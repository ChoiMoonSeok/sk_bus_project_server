from flask import request
from flask_restx import Resource, Api, Namespace

count = 1
acc_x = {}
acc_y = {}

Acc = Namespace('acc_data')

@Acc.route('')
class AccPost(Resource):
    def post(self):
        global count
        global acc_datas_raw

        idx = count
        count += 1
        acc_x[idx] = request.json.get('acc_x')
        acc_y[idx] = request.json.get('acc_y')

        return {'acc_id' : idx, 'acc_x' : acc_x[idx], 'acc_y': acc_y[idx]}

@Acc.route('/<int:acc_id>')
class AccSimple(Resource):
    def get(self, acc_id):
        return {
            'acc_id' : acc_id,
            'acc_x': acc_x[acc_id],
            'acc_y': acc_y[acc_id]
        }

    def put(self, acc_id):
        acc_x[acc_id] = request.json.get('acc_x')
        acc_y[acc_id] = request.json.get('acc_y')
        return {
            'acc_id': acc_id,
            'acc_x': acc_x[acc_id],
            'acc_y': acc_y[acc_id]
        }

    def delete(self, acc_id):
        del acc_x[acc_id]
        del acc_y[acc_id]
        return {
            'delete':'success'
        }
