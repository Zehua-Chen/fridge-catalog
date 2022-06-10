import { immerable, produce, Draft } from 'immer';

export class Method {
  static base = new Method();

  readonly name: string = '';

  [immerable] = true;

  private constructor() {}
}

export async function getMethods(): Promise<Method[]> {
  const methodsJson = await fetch(`/api/v1/methods`).then((response) =>
    response.json()
  );

  return produce([] as Method[], (methodsDraft) => {
    methodsDraft.push(
      ...methodsJson.map((methodJson: any) =>
        produce(Method.base, (methodDraft) => {
          methodDraft.name = methodJson.name;
        })
      )
    );
  });
}

export async function createMethod(
  recipe: (draft: Draft<Method>) => void
): Promise<Method> {
  const method = produce(Method.base, recipe);

  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: method.name,
    }),
  };

  const response = await fetch('/api/v1/methods', request);

  if (response.status !== 201) {
    throw new Error(response.statusText);
  }

  return method;
}
