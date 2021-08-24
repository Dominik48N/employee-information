from flask import Flask
from flask_restful import Api
import database
import atexit
import employee
import logs
import users

app = Flask(__name__)
api = Api(app)

api.add_resource(employee.Employee, "/employee/<string:first_name>_<string:last_name>")
api.add_resource(users.User, "/users/<string:name>")
api.add_resource(logs.Log, "/logs/")

app.run(debug=True)

atexit.register(database.disconnect_mysql())
