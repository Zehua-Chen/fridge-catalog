# Fridge Catalog

![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Manages the content of your fridge

## Features

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
  - [x] View Calories, Nutritional Values and Allergens of Items Removed From
        Database
- **View/Edit** (@Zehua-Chen)
  - [x] View Items
  - [x] Edit Items
  - [x] Find Items in a Location
  - [x] View Location of an Item
- **Bills**(@RubyRong)
  - [x] Calculate Bills

## Development

1. `cd web && pnpm start` to start development server
2. `FLASK_ENV=development flask run -p 4000` to start the API server

### Build

1. `cd web && pnpm build`

## Acknolwedgement

This project was originally developed as the final project of COMS 4111 at
Columbia. See [README.old.md](README.old.md) for the original README.

The project was developed by

- [Zehua Chen](https://github.com/Zehua-Chen)
- [Xingchen Rong](https://github.com/RubyRong)
