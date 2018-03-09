from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

parser = reqparse.RequestParser()
parser.add_argument('studentcode')

def convertToBinary(n):
   return bin(n)[2:]
class studentcodeToBinary(Resource):
        def post(self):
                args = parser.parse_args()
                studentcode = args['studentcode']
                studentcode_d = int(studentcode)
                studentcode_b = convertToBinary(studentcode_d)
                
                return {"studentcode":studentcode_b}

api.add_resource(studentcodeToBinary,'/api/studentcode-to-binary')


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)