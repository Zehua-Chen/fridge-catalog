import { immerable, produce } from 'immer';

export class User {
  uid: number = -1;
  name: string = '';

  [immerable] = true;
}

export async function getUsers(): Promise<User[]> {
  const usersJson = (await fetch('/api/v1/users').then((response) =>
    response.json()
  )) as any[];

  return produce([] as User[], (draft) => {
    const newUsers = usersJson.map((userJson) => {
      const user = new User();
      user.uid = userJson.uid;
      user.name = userJson.name;

      return user;
    });

    draft.push(...newUsers);
  });
}

export async function createUser(name: string, uid: string): Promise<User[]> {
  const request: RequestInit = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      uid,
      name,
    }),
  };
  const usersJson = (await fetch('/api/v1/users', request).then((response) =>
    response.json()
  )) as any[];

  return produce([] as User[], (draft) => {
    const newUsers = usersJson.map((userJson) => {
      const user = new User();
      user.uid = userJson.uid;
      user.name = userJson.name;

      return user;
    });

    draft.push(...newUsers);
  });
}
