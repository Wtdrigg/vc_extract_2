from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

"""
This file contains the code to run the todo app's API and database. The API is made using flask_restful and
database is made using flask_sqlalchemy.
"""

# Creates the Flask app object and the API and Database wrappers.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
api = Api(app)

# This variable is used as a parameter for the @marshall_with decorator used later.
resource_fields = {'id': fields.Integer,
                   'todo': fields.String,
                   }

vendor_resource_fields = {'id': fields.Integer,
                          'vendor_name': fields.String,
                          }


# This class is lays out the structure of a SQL database table. The is named after the class (in snake casing) and each
# object within the class represents a column in the database.
class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(100), nullable=False)


class VendorsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(200), nullable=False)


# with app.app_context():
#    db.create_all()


# This class is used to parse through the packages received via HTTP and structures them in JSON format
# for easy reading later.
class TodoArgumentParser:

    def __init__(self):
        self.request_args = reqparse.RequestParser()
        self.request_args.add_argument('id', type=int, help='id not found', required=True, location='form')
        self.request_args.add_argument('todo', type=str, help='todo not found', required=True, location='form')

        self.update_args = reqparse.RequestParser()
        self.update_args.add_argument('id', type=int, help='id not found', location='form')
        self.update_args.add_argument('todo', type=str, help='name not found', location='form')


class VendorArgumentParser:

    def __init__(self):
        self.request_args = reqparse.RequestParser()
        self.request_args.add_argument('id', type=int, help='id not found', required=True, location='form')
        self.request_args.add_argument('vendor_name', type=str, help='vendor_name not found', required=True,
                                       location='form')

        self.update_args = reqparse.RequestParser()
        self.update_args.add_argument('id', type=int, help='id not found', location='form')
        self.update_args.add_argument('vendor_name', type=str, help='vendor_name not found', location='form')


# This is a Resource subclass, which determines how the API will respond to different HTTP methods that are sent to
# the appropriate URI endpoint.
class TodoResource(Resource):

    # Responds to get requests by sending back the entire stored database in JSON format. If the database is empty,
    # A blank JSON file will be returned
    @marshal_with(resource_fields)
    def get(self):
        result = ToDoModel.query.all()
        return result, 200

    # Responds to put requests. Data received with the request is added to the database. Will return a
    # 404 code if the provided ID number already exists in the database.
    @marshal_with(resource_fields)
    def put(self):
        parser = TodoArgumentParser()
        args = parser.request_args.parse_args()
        todo = ToDoModel(id=args['id'], todo=args['todo'])
        result = ToDoModel.query.filter_by(id=args['id']).first()
        if result:
            abort(409, message='ID provided already exists')
        db.session.add(todo)
        db.session.commit()
        return todo, 201

    # Responds to patch requests. This is used to remove to-dos from the database. Will return a 404
    # code if the ID included with the request is not found in the database.
    @marshal_with(resource_fields)
    def patch(self):
        parser = TodoArgumentParser()
        args = parser.update_args.parse_args()
        result = ToDoModel.query.filter_by(id=args['id']).first()
        if not result:
            abort(404, message="ID provided does not exist")
        db.session.delete(result)
        db.session.commit()
        return result, 201


# This is a Resource subclass, which determines how the API will respond to different HTTP methods that are sent to
# the appropriate URI endpoint.
class VendorResource(Resource):

    # Responds to get requests by sending back the entire stored database in JSON format. If the database is empty,
    # A blank JSON file will be returned
    @marshal_with(vendor_resource_fields)
    def get(self):
        result = VendorsModel.query.all()
        return result, 200

    # Responds to put requests. Data received with the request is added to the database. Will return a
    # 404 code if the provided ID number already exists in the database.
    @marshal_with(vendor_resource_fields)
    def put(self):
        parser = VendorArgumentParser()
        args = parser.request_args.parse_args()
        vendor = VendorsModel(id=args['id'], vendor_name=args['vendor_name'])
        result = VendorsModel.query.filter_by(id=args['id']).first()
        if result:
            abort(409, message='ID provided already exists')
        db.session.add(vendor)
        db.session.commit()
        return vendor, 201

    # Responds to patch requests. This is used to remove to-dos from the database. Will return a 404
    # code if the ID included with the request is not found in the database.
    @marshal_with(vendor_resource_fields)
    def patch(self):
        parser = VendorArgumentParser()
        args = parser.update_args.parse_args()
        result = VendorsModel.query.filter_by(id=args['id']).first()
        if not result:
            abort(404, message="ID provided does not exist")
        db.session.delete(result)
        db.session.commit()
        return result, 201


# Adds the endpoint to the URI. This is the endpoint that is serviced by the prior TodoResource class.
api.add_resource(TodoResource, "/todo")
api.add_resource(VendorResource, "/vendors")

if __name__ == '__main__':
    # **IMPORTANT**
    # The db.create_all() method creates the database and must be run the first time the API is activated.
    # On all subsequent activations this should be either deleted or commented out, otherwise it will overwrite your
    # previous database with a new blank database.

    with app.app_context():
        db.create_all()

        # app.run()
