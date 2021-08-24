from flask import Flask
from flask_restful import Api
import database
import atexit
import employee
import users

app = Flask(__name__)
api = Api(app)

api.add_resource(employee.Employee, "/employee/<string:first_name>_<string:last_name>")
api.add_resource(users.User, "/users/<string:name>")

app.run(debug=True)

atexit.register(database.disconnect_mysql())
