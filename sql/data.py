from typing import Dict, Set


def sql_str_literal(s: str) -> str:
    return s.replace("'", "''")


class Row:
    _primary_keys: Dict[str, Set[object]] = {}

    def __init__(self, primary_key: object) -> None:
        class_name = str(self.__class__)

        if class_name not in Row._primary_keys:
            Row._primary_keys[class_name] = set()

        keys = Row._primary_keys[class_name]

        if primary_key in keys:
            raise Exception("duplicated primary_key: {}".format(primary_key))

        keys.add(primary_key)


class User(Row):
    _next_id = 0

    @staticmethod
    def new(name: str) -> "User":
        id = User._next_id
        User._next_id += 1

        return User(name=name, id=id)

    def __init__(self, id: int, name: str) -> None:
        super(User, self).__init__(primary_key=id)

        self.name = sql_str_literal(name)
        self.id = id

    def __str__(self) -> str:
        return "INSERT INTO Users VALUES ('{}', {});".format(self.name, self.id)


class Market(Row):
    def __init__(self, name: str, location: str) -> None:
        super(Market, self).__init__(primary_key=name)
        self.name = sql_str_literal(name)
        self.location = sql_str_literal(location)

    def __str__(self) -> str:
        return "INSERT INTO Markets VALUES ('{}', '{}');".format(self.name, self.location)


class Compartment(Row):
    def __init__(self, level: int, temperature: float) -> None:
        super(Compartment, self).__init__(primary_key=level)
        self.level = level
        self.temperature = temperature

    def __str__(self) -> str:
        return "INSERT INTO Compartments VALUES ({}, {});".format(self.level, self.temperature)


class Item(Row):
    _next_id = 0

    def new(
            name: str,
            price: float,
            amount: int,
            calories: int,
            purchase: str,
            use_by: str,
            level: Compartment,
            market: Market) -> "Item":
        new_id = Item._next_id
        Item._next_id += 1

        return Item(
            id=new_id,
            name=name,
            price=price,
            amount=amount,
            calories=calories,
            purchase=purchase,
            use_by=use_by,
            level=level,
            market=market)

    def __init__(
            self,
            id: int,
            name: str,
            price: float,
            amount: int,
            calories: int,
            purchase: str,
            use_by: str,
            level: Compartment,
            market: Market) -> None:
        super(Item, self).__init__(primary_key=id)
        self.name = sql_str_literal(name)
        self.id = id
        self.price = price
        self.amount = amount
        self.calories = calories
        self.purchase = purchase
        self.use_by = use_by
        self.level = level
        self.market = market

    def __str__(self) -> str:
        return "INSERT INTO Items VALUES ('{}', {}, {}, {}, {}, '{}', '{}', {}, '{}');".format(
            self.name,
            self.id,
            self.price,
            self.amount,
            self.calories,
            self.purchase,
            self.use_by,
            self.level.level,
            self.market.name)


class Nutrient(Row):
    def __init__(self, name: str) -> None:
        super().__init__(primary_key=name)
        self.name = sql_str_literal(name)

    def __str__(self) -> str:
        return "INSERT INTO Nutrients VALUES ('{}');".format(self.name)


class PreparationMethod(Row):
    def __init__(self, name: str) -> None:
        super().__init__(primary_key=name)
        self.name = sql_str_literal(name)

    def __str__(self) -> str:
        return "INSERT INTO PreparationMethods VALUES ('{}');".format(self.name)


class Allergen(Row):
    def __init__(self, name: str) -> None:
        super().__init__(primary_key=name)
        self.name = sql_str_literal(name)

    def __str__(self) -> str:
        return "INSERT INTO Allergens VALUES ('{}');".format(self.name)


class Ownership(Row):
    def __init__(self, user: User, item: Item, share: float) -> None:
        super().__init__(primary_key=(user.id, item.id))
        self.user = user
        self.item = item
        self.share = share

    def __str__(self) -> str:
        return "INSERT INTO Ownership VALUES ({}, {}, {});".format(
            self.user.id,
            self.item.id,
            self.share)


class Consumes(Row):
    def __init__(self, user: User, item: Item, amount: float) -> None:
        super().__init__(primary_key=(user.id, item.id))
        self.user = user
        self.item = item
        self.amount = amount

    def __str__(self) -> str:
        return "INSERT INTO Consumes VALUES ({}, {}, {});".format(
            self.user.id,
            self.item.id,
            self.amount)


class ContainsNutrient(Row):
    def __init__(self, item: Item, nutrient: Nutrient) -> None:
        super().__init__(primary_key=(item.id, nutrient.name))
        self.item = item
        self.nutrient = nutrient

    def __str__(self) -> str:
        return "INSERT INTO ContainsNutrient VALUES ({}, '{}');".format(
            self.item.id,
            self.nutrient.name)


class ContainsAllergen(Row):
    def __init__(self, item: Item, allergen: Allergen) -> None:
        super().__init__(primary_key=(item.id, allergen.name))
        self.item = item
        self.allergen = allergen

    def __str__(self) -> str:
        return "INSERT INTO ContainsAllergen VALUES ({}, '{}');".format(
            self.item.id,
            self.allergen.name)


class Preparation(Row):
    def __init__(self, item: Item, method: PreparationMethod) -> None:
        super().__init__(primary_key=(item.id, method.name))
        self.item = item
        self.method = method

    def __str__(self) -> str:
        return "INSERT INTO Preparation VALUES ({}, '{}');".format(
            self.item.id,
            self.method.name)


def main() -> None:
    print("--Generated by data.py, do not modify")

    zehua = User.new("Zehua")
    xingchen = User.new("Xingchen")

    print(zehua)
    print(xingchen)

    trader_joes = Market(
        name="Trader Joe's on Jackson Ave",
        location="2243 Jackson Ave, Long Island City, NY, 11101")

    target = Market(
        name="Target on Queens Blvd",
        location="88-01 Queens Blvd, Elmhurst, NY, 11373")

    print(trader_joes)
    print(target)

    freezer = Compartment(0, -10.0)
    fridge = Compartment(1, 10.0)

    print(freezer)
    print(fridge)

    eggs = Item.new(
        name="Eggs",
        price=5.49,
        amount=12,
        calories=66,
        purchase="2021-10-10",
        use_by="2021-11-1",
        level=fridge,
        market=trader_joes)

    squash = Item.new(
        name="Squash",
        price=2.0,
        amount=1,
        calories=82.0,
        purchase="2021-10-10",
        use_by="2022-1-1",
        level=fridge,
        market=trader_joes)

    steaks = Item.new(
        name="Steaks",
        price=12.99,
        amount=2,
        calories=160,
        purchase="2021-10-10",
        use_by="2021-10-20",
        level=freezer,
        market=target)

    print(eggs)
    print(squash)
    print(steaks)

    vitamin_d = Nutrient("Vitamin D")
    zinc = Nutrient("Zinc")

    print(vitamin_d)
    print(zinc)

    steak_seasoning = PreparationMethod("Steak Seasoning")
    boiled = PreparationMethod("Boiled")

    print(steak_seasoning)
    print(boiled)

    blackpepper_allergen = Allergen("Black Pepper")

    print(blackpepper_allergen)

    zehua_eggs = Ownership(zehua, eggs, 0.5)
    zehua_steaks = Ownership(zehua, steaks, 1.0)
    xingchen_eggs = Ownership(xingchen, eggs, 0.5)

    print(zehua_eggs)
    print(zehua_steaks)
    print(xingchen_eggs)

    zehua_eat_eggs = Consumes(zehua, eggs, 1.0)

    print(zehua_eat_eggs)

    eggs_vitamind_d = ContainsNutrient(eggs, vitamin_d)
    steaks_zinc = ContainsNutrient(steaks, zinc)

    print(eggs_vitamind_d)
    print(steaks_zinc)

    steak_seasoning_preparation = Preparation(steaks, steak_seasoning)
    steak_blackpepper_allergen = ContainsAllergen(steaks, blackpepper_allergen)

    print(steak_seasoning_preparation)
    print(steak_blackpepper_allergen)


if __name__ == "__main__":
    main()
