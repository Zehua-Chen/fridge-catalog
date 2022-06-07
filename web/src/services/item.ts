import { immerable, produce } from 'immer';

function dateToString(date: Date): string {
  const year = date.getFullYear();
  const month = date.getMonth();
  const d = date.getDate();

  const monthString = month < 10 ? `0${month}` : `${month}`;
  const dateString = d < 10 ? `0${d}` : `${d}`;

  return `${year}-${monthString}-${dateString}`;
}

export class Item {
  name: string = 'New Item';
  price: number = 1;
  amount: number = 1;
  calories: number = 0;
  mname: string = '';
  clevel: number = 0;
  purchase: string;
  useBy: string;

  [immerable] = true;

  constructor() {
    const purchase = new Date();
    const useBy = new Date();

    useBy.setDate(purchase.getDate() + 2);

    this.purchase = dateToString(purchase);
    this.useBy = dateToString(useBy);
  }
}

export async function getItem(id: number): Promise<Item> {
  const response = await fetch(`/api/item/${id}`);
  const existingItem = await response.json();

  return produce(new Item(), (draft) => {
    draft.name = existingItem.name;
    draft.price = existingItem.price;
    draft.amount = existingItem.amount;
    draft.calories = existingItem.calories;
    draft.purchase = existingItem.purchsae;
    draft.useBy = existingItem.use_by;
    draft.mname = existingItem.mname;
  });
}
