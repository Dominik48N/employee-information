from flask import Flask
from flask_restful import Api, Resource
import database
import atexit


app = Flask(__name__)
api = Api(app)
app.run(debug=True)

atexit.register(database.disconnect_mysql())
