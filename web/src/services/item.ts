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
