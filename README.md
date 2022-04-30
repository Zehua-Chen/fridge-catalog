# COMS 4111 Project 1

- DB Account: zc2616
- **Add/Remove Users, Add Items**: (@Zehua-Chen)
  - [x] Add User
  - [x] View Users
  - [x] Add Items
  - [x] Add Preparation Methods
  - [x] Remove Preparation Methods
  - [x] View Preparation Methods
  - [x] Add Location
  - [x] Put Item in Location
  - [x] Share Items Among Users
  - [x] Add Market
  - [x] Add Nutrient
  - [x] Add Nutrient to an Item
  - [x] Remove Nutrient from an Item
- **Remove** (@RubyRong)
  - [x] Remove Items
  - [x] Record Consumption
  - [x] View Calories, Nutritional Values and Allergens of Items Removed From Database
- **View/Edit** (@Zehua-Chen)
  - [x] View Items
  - [x] Edit Items
  - [x] Find Items in a Location
  - [x] View Location of an Item
- **Bills**(@RubyRong)
  - [x] Calculate Bills

We were not able to implement changing the name of preparation methods. As
the name of preparation methods are also used as their primary keys, we couldn't
implement this feature without much modifications to our ER design and SQL
tables.

## Two Interesting Page

### Create Item Page

```
/dashboard/add_item/<uid>
```

The page is used for creating new items. there are multiple select operations
used to get information like markets and fridge compartments, which are used
to popoulate UI elements, and one insert operation used to insert a new item
using user specified information, including market and fridge compartment
information. This page is interesting because it first fetch data and then use
that data to perform an insertion, whereas the most straightforward way might
be to just perform one insertion and don't use a UI element that need
data.

### Sharing Page

Sharing page is used to share an item between two users. In order to implement
this, one selection is used to get the original share of the original owner,
an update is used to adjust the share of the original user and an insert
is used to create a new ownership entity for the new owner. This page is
intersting because the desired effect is not performed with just insert or
just update, but by using a mixture of these two.

## Demo

Hosted on [Google Cloud](http://35.185.22.82:8111/)

### Starting the Production Server

1. Make a copy of `start.template.sh` and name it `start.sh`
2. Comment out the first line to enable production server
3. Add username and password to database in `start.sh`
4. Replace the last line with `flask run -p 8111 -h 0.0.0.0`
5. `sh start.sh` and the server will be hosted at the above address

## Development

1. Make a copy of `start.template.sh`, and name it to `start.sh`
2. Add username and password to `start.sh`
3. `sh start.sh` and the frontend will be hosted at: [`http://127.0.0.1:5000`](http://127.0.0.1:5000)

### Using VSCode

Open this project in a container

### Not Using VSCode

Go to `.devcontainer` and use docker compose
