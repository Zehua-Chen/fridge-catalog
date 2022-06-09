import { immerable, produce, Draft } from 'immer';

export class User {
  static base = new User();

  readonly uid: number = -1;
  readonly name: string = '';

  [immerable] = true;

  private constructor() {}
}

export async function getUsers(): Promise<User[]> {
  const usersJson = (await fetch('/api/v1/users').then((response) =>
    response.json()
  )) as any[];

  return produce([] as User[], (draft) => {
    const newUsers = usersJson.map((userJson) => {
      return produce(User.base, (draft) => {
        draft.uid = userJson.uid;
        draft.name = userJson.name;
      });
    });

    draft.push(...newUsers);
  });
}

export async function createUser(
  recipe: (draft: Draft<User>) => void
): Promise<User> {
  const user = produce(User.base, recipe);
  const request: RequestInit = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      uid: user.uid,
      name: user.name,
    }),
  };

  const response = await fetch('/api/v1/users', request);

  if (response.status !== 201) {
    throw Error(response.statusText);
  }

  return user;
}
