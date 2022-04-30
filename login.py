import paths
import status
import sqlalchemy as sql

from flask import Blueprint, Response, render_template, jsonify, g, request


login = Blueprint("login", "login", template_folder=paths.template_dir())


@login.route("/api/users")
def api_users():
    with g.engine.connect() as connection:
        def user_row_to_dict(row):
            return {"name": row["name"], "uid": row["uid"]}

        rows = connection.execute(sql.text("SELECT * FROM Users"))

        users = list(map(user_row_to_dict, rows))

        return jsonify(users)


@login.route("/api/user", methods=["POST"])
def api_post_user():
    """
    Create a new user
    """
    name = request.args["name"]
    uid = int(request.args["uid"])

    with g.engine.connect() as connection:
        connection.execute(
            sql.text(f"INSERT INTO Users (name, uid) VALUES ('{name}', {uid})"))

        return Response(status=status.created())


@login.route("/")
def index():
    """
    Route: /
    Render a list of users for user to "log in"
    """
    return render_template("index.html")
