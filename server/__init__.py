from flask import Flask, request
from flask_restx import Api, Resource
from acc_data import Acc

app = Flask(__name__) 
api = Api(app) # api 모듈 호출

api.add_namespace(Acc, '/acc_data') # acc_data 파일에 정의한 api 가져오기

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) # 설정한 주소로 서버 열기