#create REST API service to receive new data and store it in a database
#and create a REST API service to retrieve data from the database

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonpify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Update_Employee(Resource):
    def put(self, employee_id):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        TitleOfCourtesy = request.json['TitleOfCourtesy']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        Region = request.json['Region']
        PostalCode = request.json['PostalCode']
        Country = request.json['Country']
        HomePhone = request.json['HomePhone']
        Extension = request.json['Extension']
        Photo = request.json['Photo']
        Notes = request.json['Notes']
        ReportsTo = request.json['ReportsTo']
        PhotoPath = request.json['PhotoPath']
        query = conn.execute("update employees set LastName = '%s', FirstName = '%s', Title = '%s', TitleOfCourtesy = '%s', BirthDate = '%s', HireDate = '%s', Address = '%s', City = '%s', Region = '%s', PostalCode = '%s', Country = '%s', HomePhone = '%s', Extension = '%s', Photo = '%s', Notes = '%s', ReportsTo = '%s', PhotoPath = '%s' where EmployeeId =%d"
        %(str(LastName),str(FirstName),str(Title),str(TitleOfCourtesy),str(BirthDate),str(HireDate),str(Address),str(City),str(Region),str(PostalCode),str(Country),str(HomePhone),str(Extension),str(Photo),str(Notes),str(ReportsTo),str(PhotoPath),int(employee_id)))
        return {'status':'success'}