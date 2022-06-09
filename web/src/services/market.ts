import { immerable, produce, Draft } from 'immer';

export class Market {
  static base = new Market();

  readonly name: string = '';
  readonly location: string = '';

  [immerable] = true;

  private constructor() {}
}

export async function getMarkets(): Promise<Market[]> {
  const marketsJson = await fetch('/api/v1/markets').then((response) =>
    response.json()
  );

  return produce([] as Market[], (draft) => {
    draft.push(
      ...marketsJson.map((marketJson: any) => {
        return produce(Market.base, (draft) => {
          draft.name = marketJson.name;
          draft.location = marketJson.location;
        });
      })
    );
  });
}

export async function createMarket(
  recipe: (draft: Draft<Market>) => void
): Promise<Market> {
  const market = produce(Market.base, recipe);

  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: market.name,
      location: market.location,
    }),
  };

  const response = await fetch('/api/v1/markets', request);

  if (response.status !== 201) {
    throw new Error(response.statusText);
  }

  return market;
}
