import { immerable, produce } from 'immer';

export class Compartment {
  clevel: number = -1;
  temperature: number = 0;

  [immerable] = true;
}

export async function getCompartments(): Promise<Compartment[]> {
  const compartmentsJson = (await fetch('/api/compartments').then((response) =>
    response.json()
  )) as any[];

  return produce([] as Compartment[], (draft) => {
    const newCompartments = compartmentsJson.map((compartmentJson) => {
      const compartment = new Compartment();
      compartment.clevel = compartmentJson.clevel;

      return compartment;
    });

    draft.push(...newCompartments);
  });
}
