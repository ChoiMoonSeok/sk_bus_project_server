from datetime import datetime
from xmlrpc.client import DateTime
from flask import request
from flask_restx import Resource, Api, Namespace

count = 1
acc_x = {} # x축 가속도를 저장할 {}
acc_y = {} # y축 가속도를 저장할 {}

Acc = Namespace('acc_data')

@Acc.route('')
class AccPost(Resource):
    def post(self): # post 함수 정의, 데이터 입력
        global count
        global acc_datas_raw

        idx = count
        count += 1
        acc_x[idx] = float(request.json.get('acc_x')) # json을 받아서 float으로 변환 후 {}에 저장
        acc_y[idx] = float(request.json.get('acc_y')) # json을 받아서 float으로 변환 후 {}에 저장

        return {'acc_id' : idx, 'acc_x' : acc_x[idx], 'acc_y': acc_y[idx]}

    def get(self): # get 함수 정의, 데이터 입력
        return {'acc_id': count-1, 'acc_x' : acc_x[count-1], 'acc_y': acc_y[count-1]}


@Acc.route('/<int:acc_id>') # acc_id에 맞는 데이터 조회
class AccSimple(Resource):
    def get(self, acc_id): # 데이터 가져오기
        return {
            'acc_id' : acc_id,
            'acc_x': acc_x[acc_id],
            'acc_y': acc_y[acc_id],
        }


    def put(self, acc_id): # 데이터 수정하기
        acc_x[acc_id] = request.json.get('acc_x')
        acc_y[acc_id] = request.json.get('acc_y')
        return {
            'acc_id': acc_id,
            'acc_x': acc_x[acc_id],
            'acc_y': acc_y[acc_id],
        }
 
    def delete(self, acc_id): # 데이터 삭제하기
        del acc_x[acc_id]
        del acc_y[acc_id]
        return {
            'delete':'success'
        }
