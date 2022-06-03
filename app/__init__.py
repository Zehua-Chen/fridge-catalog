"""
Web server for Project 1, Part 3.
"""

import os
import flask
import flask.logging
from flask.templating import render_template
import sqlalchemy as sql

from flask import g, current_app, request, Flask, jsonify, request

from flask import g
from app.db import init_db
from app.dashboard import dashboard
from app.login import login

template_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'templates')


app = flask.Flask(
    __name__,
    template_folder=template_dir,
    static_folder='../static',
    static_url_path='/app')

app.register_blueprint(dashboard)
app.register_blueprint(login)


@app.before_request
def before_request():
    init_db()


@app.route("/record")
def recordConsumption():
    return flask.render_template("record.html")


@app.route("/record/<name>/<food>/<number>")
def makeRecord(name, food, number):

    # update the consumptionlist:
    with g.engine.connect() as connection:
        u1 = connection.execute(
            sql.text(f"SELECT users.uid FROM users WHERE users.name = '{name}'"))
        for u in u1:
            uid = u["uid"]
        i1 = connection.execute(
            sql.text(f"SELECT items.iid FROM items WHERE items.name = '{food}'"))
        for u in i1:
            iid = u["iid"]
        # get the amount in database:
        temp = connection.execute(
            sql.text(f"SELECT consumes.amount FROM consumes WHERE consumes.iid = '{iid}'"))
        tmp = 0
        for u in temp:
            tmp = u["amount"]
        ans = number
        ans = int(tmp) - int(number)
        connection.execute(sql.text(
            f"UPDATE consumes SET  amount = {ans} WHERE iid = {iid} and uid = {uid} "))
        print(iid)

        nutrition = connection.execute(sql.text(
            f"SELECT containsnutrient.nname FROM containsnutrient WHERE containsnutrient.iid = '{iid}'"))
        nutritions = []
        for nu in nutrition:
            nutritions.append(nu["nname"])
            print(nu["nname"])
        print("-----------------------------", nutritions, iid)
        allergy = connection.execute(sql.text(
            f"SELECT containsallergen.aname FROM containsallergen WHERE containsallergen.iid = '{iid}'"))
        allergens = []
        for nu in allergy:
            allergens.append(nu["aname"])
        calorie = connection.execute(
            sql.text(f"SELECT items.calories FROM items WHERE items.iid = '{iid}'"))

        calories = 0
        for nu in calorie:
            calories = nu["calories"]

    # get the nutrition info:
    calories = int(calories) * int(number)

    return {"calories": calories, "nutritions": nutritions, "allergens": allergens}


@app.route("/checkPay")
def checkpay():
    return flask.render_template("getbill.html")


@app.route("/checkPay/bill/<nameFrom>/<nameTo>")
def getbill(nameFrom, nameTo):

    # fetch the price need to pay in the database according to the namefrom and nameto
    with g.engine.connect() as connection:
        # get uid from name:

        u1 = connection.execute(
            sql.text(f"SELECT users.uid FROM users WHERE users.name = '{nameFrom}'"))
        u2 = connection.execute(
            sql.text(f"SELECT users.uid FROM users WHERE users.name = '{nameTo}'"))
        for u in u1:
            uid1 = u["uid"]
        for u in u2:
            uid2 = u["uid"]

        rows = connection.execute(sql.text(f"""SELECT iid FROM (SELECT ownership.uid, ownership.iid
                                FROM ownership WHERE ownership.uid ={uid1} or ownership.uid = {uid2} )AS t GROUP BY iid HAVING COUNT(*) = 2"""))

        # get the price for each food
        foods = list(map(lambda row: row["iid"], rows))

        def item_to_price(row):
            return {"item": row["price"]}

        itemprices = {}
        for itemID in foods:
            price = connection.execute(sql.text(
                f"""SELECT items.iid, items.price FROM items WHERE items.iid = {itemID}"""))
            for row in price:
                itemprices[row["iid"]] = row["price"]

        consumeHistory = {}

        for itemID in foods:

            amount = connection.execute(sql.text(
                f"""SELECT consumes.iid, consumes.amount FROM consumes WHERE consumes.iid = {itemID} AND consumes.uid = {uid1}"""))

            for row in amount:
                consumeHistory[row["iid"]] = row["amount"]
        print("-------------", itemprices, consumeHistory)
        # itemprice{item: prices}
        # consumHistory{item: ammount}  item prices * item amount = fee
        fee = 0
        for item in foods:
            fee += itemprices[item] * consumeHistory[item]
        res = {"price": fee}
    return res


@app.route("/dashboard/remove/<uid>")
def remove(uid):
    return flask.render_template("removeItem.html", uid=uid)


@app.route("/remove/<uid>", methods=["GET", "DELETE"])
def removeItem(uid):
    # extract the food ownered by the uid:

    with g.engine.connect() as connection:
        # get uid from name:

      #  uid = 1

        response_object = {'status': 'success'}
        if request.method == "DELETE":
            deletFood = request.get_json()
            print("go through here", deletFood["foodID"])
            # delet to the databse
            iid = deletFood["foodID"]
            connection.execute(
                sql.text(f"DELETE FROM containsnutrient WHERE containsnutrient.iid = {iid} "))
            connection.execute(
                sql.text(f"DELETE FROM ownership WHERE ownership.iid = {iid} "))
            connection.execute(
                sql.text(f"DELETE FROM items WHERE items.iid = {iid} "))

        foods = connection.execute(sql.text(
            f"SELECT items.iid, items.name FROM items LEFT OUTER JOIN ownership ON items.iid = ownership.iid WHERE ownership.uid = {uid} "))

        foodlist = []
        for row in foods:
            foodlist.append({"name": row["name"], "id": row["iid"]})

    return jsonify(foodlist)
