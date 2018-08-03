# -*- coding: utf-8 -*-
import sys

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask_restful import reqparse, Resource, Api
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'pegue891_develop'
app.config['MYSQL_DATABASE_PASSWORD'] = 'develop'
app.config['MYSQL_DATABASE_DB'] = 'pegue891_4worktime'
app.config['MYSQL_DATABASE_HOST'] = 'www.visiblenet.com.br'
app.config['MYSQL_DATABASE_PORT'] = 3306

api = Api(app)
mysql.init_app(app)



class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            #'criando conexão com o banco'
            conn = mysql.connect()

            _userEmail = args['email']
            _userPassword = args['password']

            print _userEmail
            print _userPassword

            cursor = conn.cursor()
            cursor.callproc('spCreateUser', (_userEmail, _userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    app.run(debug=True, port=1606)