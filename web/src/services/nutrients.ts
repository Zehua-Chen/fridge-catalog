import { immerable, produce, Draft } from 'immer';

export class Nutrient {
  static base = new Nutrient();

  readonly name: string = '';

  [immerable] = true;

  private constructor() {}
}

export async function getNutrients(): Promise<Nutrient[]> {
  const nutrientsJson = await fetch('/api/v1/nutrients').then((response) =>
    response.json()
  );

  return produce([] as Nutrient[], (draft) => {
    draft.push(
      ...nutrientsJson.map((marketJson: any) => {
        return produce(Nutrient.base, (draft) => {
          draft.name = marketJson.name;
        });
      })
    );
  });
}

export async function createNutrient(
  recipe: (draft: Draft<Nutrient>) => void
): Promise<Nutrient> {
  const nutrient = produce(Nutrient.base, recipe);

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

  return nutrient;
}
