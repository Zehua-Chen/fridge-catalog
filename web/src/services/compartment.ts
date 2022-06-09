import { immerable, produce, Draft } from 'immer';

export class Compartment {
  static base = new Compartment();

  readonly level: number = -1;
  readonly temperature: number = 0;

  [immerable] = true;

  private constructor() {}
}

export async function getCompartments(): Promise<Compartment[]> {
  const compartmentsJson = (await fetch('/api/v1/compartments').then(
    (response) => response.json()
  )) as any[];

  return produce([] as Compartment[], (draft) => {
    const newCompartments = compartmentsJson.map((compartmentJson) => {
      return produce(Compartment.base, (draft) => {
        draft.level = compartmentJson.level;
        draft.temperature = compartmentJson.temperature;
      });
    });

    draft.push(...newCompartments);
  });
}

export async function createCompartment(
  recipe: (draft: Draft<Compartment>) => void
): Promise<Compartment> {
  const compartment = produce(Compartment.base, recipe);

  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      level: compartment.level,
      temperature: compartment.temperature,
    }),
  };

  const response = await fetch('/api/v1/compartments', request);

  if (response.status !== 200) {
    throw new Error(response.statusText);
  }

  return compartment;
}
