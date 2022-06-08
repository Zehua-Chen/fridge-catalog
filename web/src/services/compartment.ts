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
      compartment.temperature = compartmentJson.temperature;

      return compartment;
    });

    draft.push(...newCompartments);
  });
}

export async function createCompartment(
  compartment: Compartment
): Promise<void> {
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
}
