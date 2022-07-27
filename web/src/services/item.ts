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
  static base = new Item();

  readonly iid: number = -1;
  readonly name: string = 'New Item';
  readonly price: number = 1;
  readonly amount: number = 1;
  readonly calories: number = 0;
  readonly mname: string = '';
  readonly clevel: number = 0;
  readonly purchase: string;
  readonly useBy: string;

  readonly share: number = 0;

  [immerable] = true;

  private constructor() {
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

  return produce(Item.base, (draft) => {
    draft.name = existingItem.name;
    draft.price = existingItem.price;
    draft.amount = existingItem.amount;
    draft.calories = existingItem.calories;
    draft.purchase = existingItem.purchsae;
    draft.useBy = existingItem.use_by;
    draft.mname = existingItem.mname;
  });
}

export async function getItems(userId: string): Promise<Item[]> {
  fetch(`/api/items/${userId}`)
    .then((response) => response.json())
    .then((value) => (items.value = value));

  return [];
}
