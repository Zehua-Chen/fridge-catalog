import os
import random
import app.status as status
import sqlalchemy as sql

from flask import Blueprint, g, json, request, render_template, jsonify
from flask.wrappers import Response
from app.strs import sql_str_literal


template_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'templates')

dashboard = Blueprint("dashboard", "dashboard", template_folder=template_dir)


def item_row_to_dict(row):
    d = {}

    if "name" in row:
        d["name"] = row["name"]

    if "price" in row:
        d["price"] = row["price"]

    if "amount" in row:
        d["amount"] = row["amount"]

    if "calories" in row:
        d["calories"] = row["calories"]

    if "purchase" in row:
        d["purchase"] = row["purchase"]

    if "use_by" in row:
        d["use_by"] = row["use_by"]

    if "mname" in row:
        d["mname"] = row["mname"]

    if "iid" in row:
        d["iid"] = row["iid"]

    if "clevel" in row:
        d["clevel"] = row["clevel"]

    if "share" in row:
        d["share"] = row["share"]

    return d


def preparation_method_row_to_dict(row):
    return {"method": row["method"]}


@dashboard.route("/api/item/<iid>", methods=["GET"])
def api_get_item(iid):
    with g.engine.connect() as connection:
        rows = connection.execute(
            sql.text(f"""
            SELECT * from Items where Items.iid = {iid}"""))

        items = list(map(item_row_to_dict, rows))
        print(items)

        return jsonify(items[0])


@dashboard.route("/api/item/<iid>", methods=["PUT"])
def api_put_item(iid):
    item = request.get_json()
    name = sql_str_literal(item["name"])
    price = float(item["price"])
    amount = int(item["amount"])
    calories = float(item["calories"])
    # purchase = item["purchase"]
    # useBy = item["useBy"]
    mname = sql_str_literal(item["mname"])

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"""
            UPDATE Items SET
                name = '{name}',
                price = {price},
                amount = {amount},
                calories = {calories},
                mname = '{mname}'
            WHERE Items.iid = {iid}"""))

        return Response(status=status.accepted())


@dashboard.route("/api/items/<uid>", methods=["GET"])
def api_get_items(uid):
    with g.engine.connect() as connection:
        rows = connection.execute(
            sql.text(f"""
            SELECT Items.iid, Items.name, Items.clevel, Ownership.share FROM Items JOIN Ownership
                ON Items.iid = Ownership.iid AND Ownership.uid = {uid}"""))

        ownedItems = list(map(item_row_to_dict, rows))

        return jsonify(ownedItems)


@dashboard.route("/api/items/<uid>", methods=["POST"])
def api_post_items(uid):
    new_item = request.get_json()

    name = sql_str_literal(new_item["name"])
    iid = random.randint(-2147483648, 2147483647)
    price = float(new_item["price"])
    amount = int(new_item["amount"])
    calories = float(new_item["calories"])
    purchase = sql_str_literal(new_item["purchase"])
    use_by = sql_str_literal(new_item["useBy"])
    clevel = int(new_item["clevel"])
    mname = sql_str_literal(new_item["mname"])

    with g.engine.connect() as connection:
        with connection.begin():
            connection.execute(
                sql.text(f"""
                INSERT INTO Items (name, iid, price, amount, calories, purchase, use_by, clevel, mname)
                VALUES ('{name}', {iid}, {price}, {amount}, {calories},
                        '{purchase}', '{use_by}', {clevel}, '{mname}');"""))

            connection.execute(
                f"INSERT INTO Ownership (uid, iid, share) VALUES ({uid}, {iid}, 1.0);")

    return Response(status=status.created())


@dashboard.route("/api/compartments", methods=["GET"])
def api_get_compartments():
    with g.engine.connect() as connection:
        rows = connection.execute(sql.text(f"SELECT * FROM Compartments"))
        compartments = list(
            map(lambda r: {"clevel": r["clevel"], "temperature": r["temperature"]}, rows))

        return jsonify(compartments)


@dashboard.route("/api/compartment", methods=["POST"])
def api_post_compartment():
    new_compartment = request.get_json()
    clevel = int(new_compartment["clevel"])
    temperature = int(new_compartment["temperature"])

    with g.engine.connect() as connection:
        connection.execute(sql.text(
            f"INSERT INTO Compartments (clevel, temperature) VALUES ({clevel}, {temperature})"))

        return Response(status=status.created())


@dashboard.route("/api/methods", methods=["GET"])
def api_get_methods():
    with g.engine.connect() as connection:
        rows = connection.execute(
            sql.text(f"""SELECT PreparationMethods.method FROM PreparationMethods"""))

        preparationMethods = list(map(preparation_method_row_to_dict, rows))

        return jsonify(preparationMethods)


@dashboard.route("/api/methods", methods=["POST"])
def api_post_methods():
    new_method = request.get_json()
    method = new_method["method"]

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"INSERT INTO PreparationMethods (method) VALUES ('{method}')"))

        return Response(status=status.created())


@dashboard.route("/api/preparations", methods=["GET"])
def api_get_preparations():
    iid = request.args["iid"]

    with g.engine.connect() as connection:
        rows = connection.execute(
            sql.text(f"""SELECT * FROM Preparation WHERE Preparation.iid = {iid}"""))

        preparations = list(
            map(lambda r: {"method": r["method"], iid: r["iid"]}, rows))

        return jsonify(preparations)


@dashboard.route("/api/preparations", methods=["POST"])
def api_post_preparations():
    preparation = request.get_json()
    iid = preparation["iid"]
    method = sql_str_literal(preparation["method"])

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"""INSERT INTO Preparation (iid, method) VALUES ({iid}, '{method}')"""))

        return Response(status=status.created())


@dashboard.route("/api/preparations", methods=["DELETE"])
def api_delete_preparations():
    iid = request.args["iid"]
    method = sql_str_literal(request.args["method"])

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"""DELETE FROM Preparation WHERE Preparation.iid = {iid} AND Preparation.method = '{method}'"""))

        return Response(status=status.accepted())


@dashboard.route("/api/markets", methods=["GET"])
def api_get_markets():
    with g.engine.connect() as connection:
        rows = connection.execute(
            sql.text(f"""SELECT * FROM Markets"""))

        markets = list(
            map(lambda r: {"mname": r["mname"], "location": r["location"]}, rows))

        return jsonify(markets)


@dashboard.route("/api/markets", methods=["POST"])
def api_post_markets():
    new_market = request.get_json()
    mname = new_market["mname"]
    location = new_market["location"]

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"INSERT INTO Markets (mname, location) VALUES ('{mname}', '{location}')"))

        return Response(status=status.created())


@dashboard.route("/api/contains_nutrient", methods=["POST"])
def api_post_contain_nutrient():
    new_market = request.get_json()
    nname = new_market["nname"]
    iid = new_market["iid"]

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"INSERT INTO ContainsNutrient (nname, iid) VALUES ('{nname}', '{iid}')"))

        return Response(status=status.created())


@dashboard.route("/api/contains_nutrient", methods=["DELETE"])
def api_delete_contain_nutrient():
    nname = request.args["nname"]
    iid = request.args["iid"]

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"DELETE FROM ContainsNutrient WHERE ContainsNutrient.nname = '{nname}' AND ContainsNutrient.iid = '{iid}'"))

        return Response(status=status.created())


@dashboard.route("/api/nutrients", methods=["GET"])
def api_get_nutrients():
    with g.engine.connect() as connection:
        if "iid" in request.args:
            iid = request.args["iid"]

            rows = connection.execute(
                sql.text(f"SELECT * FROM ContainsNutrient WHERE ContainsNutrient.iid = {iid}"))

            nutrients = list(map(lambda r: {"nname": r["nname"]}, rows))
            return jsonify(nutrients)

        rows = connection.execute(
            sql.text(f"SELECT * FROM Nutrients"))

        nutrients = list(map(lambda r: {"nname": r["nname"]}, rows))

        return jsonify(nutrients)


@dashboard.route("/api/nutrients", methods=["POST"])
def api_post_nutrients():
    new_market = request.get_json()
    nname = new_market["nname"]

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"INSERT INTO Nutrients (nname) VALUES ('{nname}')"))

        return Response(status=status.created())


@dashboard.route("/api/ownerships", methods=["POST"])
def api_post_ownership():
    new_ownership = request.get_json()

    iid = new_ownership["iid"]
    originalOwner = new_ownership["originalOwner"]
    newOwner = new_ownership["newOwner"]
    share = new_ownership["share"]

    assert share >= 0 and share <= 1

    with g.engine.connect() as connection:
        rows = connection.execute(sql.text(f"""
            SELECT Ownership.share FROM Ownership WHERE Ownership.uid = {originalOwner} AND Ownership.iid = {iid}"""))

        originalShare = list(map(lambda r: r["share"], rows))
        assert len(originalShare) == 1

        originalShare = float(originalShare[0])

        connection.execute(sql.text(f"""
            UPDATE Ownership SET share = {originalShare * (1 - share)} WHERE uid = {originalOwner} AND iid = {iid};
            INSERT INTO Ownership (uid, iid, share) VALUES ({newOwner}, {iid}, {originalShare * share})"""))

        return Response(status=status.created())


@dashboard.route("/api/move", methods=["POST"])
def api_move():
    move = request.get_json()
    iid = move["iid"]
    # originalCompartment = move["originalCompartment"]
    newCompartment = move["newCompartment"]

    with g.engine.connect() as connection:
        connection.execute(sql.text(f"""
            UPDATE Items SET clevel = {newCompartment} WHERE iid = {iid}"""))

        return Response(status=status.accepted())


@dashboard.route("/dashboard/add_item/<uid>")
def add_item(uid):
    return render_template("add_item.html", uid=uid)


@dashboard.route("/dashboard/share_item")
def share_item():
    item = request.args["item"]
    owner = request.args["owner"]

    return render_template("share_item.html", item=item, owner=owner)


@dashboard.route("/dashboard/move_item")
def move_item():
    item = request.args["item"]
    compartment = request.args["compartment"]

    return render_template("move_item.html", item=item, compartment=compartment)


@dashboard.route("/dashboard/edit_item")
def edit_item():
    iid = request.args["iid"]

    return render_template("edit_item.html", iid=iid)


@dashboard.route("/dashboard/add_compartment")
def add_location():
    return render_template("add_compartment.html")


@dashboard.route("/dashboard/add_preparation_method")
def add_preparation_method():
    return render_template("add_preparation_method.html")


@dashboard.route("/dashboard/add_market")
def add_market():
    return render_template("add_market.html")


@dashboard.route("/dashboard/prepare_item")
def prepare_item():
    iid = request.args["iid"]

    return render_template("prepare_item.html", iid=iid)


@dashboard.route("/dashboard/nutrirent_item")
def nutrient_item():
    iid = request.args["iid"]

    return render_template("nutrient_item.html", iid=iid)


@dashboard.route("/dashboard/add_nutrient")
def add_nutrient():
    return render_template("add_nutrient.html")


@dashboard.route("/dashboard/<uid>")
def index(uid):
    with g.engine.connect() as connection:

        rows = connection.execute(
            sql.text(f"SELECT Users.name FROM Users WHERE Users.uid = {uid}"))

        names = list(map(lambda row: row["name"], rows))

    assert len(names) == 1

    return render_template("dashboard.html", uid=uid, name=names[0])
