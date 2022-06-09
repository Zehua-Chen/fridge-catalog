import { immerable, produce } from 'immer';

export class Nutrient {
  name: string = '';

  [immerable] = true;
}

export async function getNutrients(): Promise<Nutrient[]> {
  const nutrientsJson = await fetch('/api/v1/nutrients').then((response) =>
    response.json()
  );

  return produce([] as Nutrient[], (draft) => {
    draft.push(
      ...nutrientsJson.map((marketJson: any) => {
        const market = new Nutrient();
        market.name = marketJson.name;

        return market;
      })
    );
  });
}

export async function createNutrient(nutrient: Nutrient): Promise<void> {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: nutrient.name,
    }),
  };

  const response = await fetch('/api/v1/nutrients', request);

  if (response.status !== 201) {
    throw new Error(response.statusText);
  }
}
