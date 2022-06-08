import { immerable, produce } from 'immer';

export class Compartment {
  level: number = -1;
  temperature: number = 0;

  [immerable] = true;
}

export async function getCompartments(): Promise<Compartment[]> {
  const compartmentsJson = (await fetch('/api/v1/compartments').then(
    (response) => response.json()
  )) as any[];

  return produce([] as Compartment[], (draft) => {
    const newCompartments = compartmentsJson.map((compartmentJson) => {
      const compartment = new Compartment();
      compartment.level = compartmentJson.level;

      return compartment;
    });

    draft.push(...newCompartments);
  });
}
