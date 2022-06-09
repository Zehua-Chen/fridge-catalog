import produce, { immerable } from 'immer';

export class Market {
  name: string = '';
  location: string = '';

  [immerable] = true;
}

export async function getMarkets(): Promise<Market[]> {
  const marketsJson = await fetch('/api/v1/markets').then((response) =>
    response.json()
  );

  return produce([] as Market[], (draft) => {
    draft.push(
      ...marketsJson.map((marketJson: any) => {
        const market = new Market();
        market.name = marketJson.name;
        market.location = marketJson.location;

        return market;
      })
    );
  });
}

export async function createMarket(market: Market): Promise<void> {
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
}
