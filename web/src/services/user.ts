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
