from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return {'data':'success'},200

api.add_resource(Index, '/api')

if __name__ == '__main__': 
    app.run(debug=True)


