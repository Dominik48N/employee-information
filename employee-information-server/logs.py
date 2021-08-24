from flask_restful import Resource, fields, marshal_with, reqparse
import database

resource_fields = {
    'type': fields.String,
    'note': fields.String,
    'date': fields.String,
    'user': fields.String
}

log_put_args = reqparse.RequestParser()
log_put_args.add_argument("type", type=str, help="Type of the log is required", required=True)
log_put_args.add_argument("note", type=str, help="Note of the log is required", required=True)
log_put_args.add_argument("date", type=str, help="Date of the log is required", required=True)
log_put_args.add_argument("user", type=str, help="User of the log is required", required=True)


class Log(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = log_put_args.parse_args()

        database.execute_sql("INSERT INTO `log`(`type`, `note`, `date`, `user`) VALUES ('{}','{}','{}','{}')"
                             .format(args['type'], args['note'], args['date'], args['user']))

        return LogModel(args['type'], args['note'], args['date'], args['user'])


class LogModel:

    def __init__(self, type, note, date, user):
        self.type = type
        self.note = note
        self.date = date
        self.user = user

    def __repr__(self):
        return "Log(type = {}, note = {}, date = {}, user = {})".format(self.type, self.note, self.date, self.user)
