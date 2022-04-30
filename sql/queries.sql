-- get the name of item and their owner. If an item is co-owned, it would
-- appear twice, but with different owners
SELECT Items.name as item_name, Users.name as user_name FROM
  Items JOIN Ownership ON Items.iid = Ownership.iid
    JOIN Users ON Ownership.uid = Users.uid;

-- average price of items owned by user 0
SELECT AVG(Items.price) as average_price_user_0 FROM Items
  WHERE Items.iid IN (SELECT Ownership.iid FROM Ownership
    WHERE Ownership.uid = 0);

-- get a list of food that contain Vitamin D
SELECT Items.name as item_vitamin_d FROM Items
  WHERE Items.iid IN (SELECT ContainsNutrient.iid FROM ContainsNutrient
    WHERE ContainsNutrient.nname = 'Vitamin D');
