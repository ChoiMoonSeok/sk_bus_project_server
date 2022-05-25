from flask import Flask, request
from flask_restx import Api, Resource
from acc_data import Acc

app = Flask(__name__)
api = Api(app)

api.add_namespace(Acc, '/acc_data')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)