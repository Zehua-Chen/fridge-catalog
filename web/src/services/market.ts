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

  console.log(marketsJson);

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
