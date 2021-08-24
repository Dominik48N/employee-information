from flask_restful import Resource, abort, fields, marshal_with
import database

resource_fields = {
    'name': fields.String,
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
        return UserModel(result[0], result[1])


class UserModel:

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __repr__(self):
        return "User(name = {}, rank = {})".format(self.name, self.rank)
