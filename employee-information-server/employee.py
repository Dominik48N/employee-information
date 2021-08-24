from flask_restful import Resource, abort, fields, marshal_with
import database

resource_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'age': fields.Integer,
    'gender': fields.String,
    'salary': fields.Integer,
    'note': fields.String,
    'job': fields.String,
    'joined_at': fields.String,
    'state': fields.Integer
}


class Employee(Resource):
    @marshal_with(resource_fields)
    def get(self, first_name, last_name):
        results = database.fetch_sql(
            "SELECT * FROM `employee` WHERE `first_name` = '{}' AND `last_name` = '{}'".format(first_name, last_name)
        )
        if not results:
            abort(404, message="Could not find employee with that name")
        result = results[0]
        return EmployeeModel(result[0],
                             result[1],
                             result[2],
                             result[3],
                             result[4],
                             result[5],
                             result[6],
                             result[7],
                             result[8],
                             result[9])


class EmployeeModel:

    def __init__(self, employee_id, first_name, last_name, age, gender, salary, note, job, joined_at, state):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.note = note
        self.job = job
        self.joined_at = joined_at
        self.state = state

    def __repr__(self):
        return "Employee(" \
               "id = {}, " \
               "first_name = {}, " \
               "last_name = {}, " \
               "age = {}, " \
               "gender = {}, " \
               "salary = {}, " \
               "note = {}, " \
               "job = {}, " \
               "joined_at = {}, " \
               "state = {}" \
               ")".format(self.employee_id,  self.first_name, self.last_name, self.age, self.gender, self.salary,
                          self.note, self.job, self.joined_at, self.state)
