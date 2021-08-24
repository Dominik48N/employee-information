from flask_restful import Resource, abort, fields, marshal_with
import database

resource_fields = {
    'name': fields.String,
    'password': fields.String,
    'rank': fields.Integer
}


class User(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        results = database.fetch_sql(
            "SELECT * FROM `users` WHERE `name` = '{}'".format(name)
        )
        if not results:
            abort(404, message="Could not find user with that name")
        result = results[0]
        return UserModel(result[0], result[1], result[2])


class UserModel:

    def __init__(self, name, password, rank):
        self.name = name
        self.password = password
        self.rank = rank

    def __repr__(self):
        return "User(name = {}, password = {}, rank = {})".format(self.name, self.password, self.rank)
