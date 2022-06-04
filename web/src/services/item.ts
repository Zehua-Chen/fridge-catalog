export interface Item {
  name: string;
  price: number;
  amount: number;
  calories: number;
  purchase: string;
  useBy: string;
  mname: string;
  clevel: number;
}

function dateToString(date: Date): string {
  const year = date.getFullYear();
  const month = date.getMonth();
  const d = date.getDate();

  const monthString = month < 10 ? `0${month}` : `${month}`;
  const dateString = d < 10 ? `0${d}` : `${d}`;

  return `${year}-${monthString}-${dateString}`;
}

export function createDefaultItem(): Item {
  const purchase = new Date();
  const useBy = new Date();

  useBy.setDate(purchase.getDate() + 2);

  return {
    name: 'New Item',
    price: 0,
    amount: 1,
    calories: 0,
    purchase: dateToString(purchase),
    useBy: dateToString(useBy),
    mname: '',
    clevel: -1,
  };
}
