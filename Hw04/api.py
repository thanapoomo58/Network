from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('studentid')

def convertToBinary(n):
   return bin(n)[2:]
class studentidToBinary(Resource):
        def post(self):
                args = parser.parse_args()
                studentid = args['studentid']
                studentid_d = int(studentid)
                studentid_b = convertToBinary(studentid_d)
                
                return {"studentid":studentid_b}

api.add_resource(studentidToBinary,'/api/studentid_to_binary')


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)
