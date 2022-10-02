import json
import time

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def post(self) -> json:
        try:
            value = 0
            req = request.get_data()
            data = json.loads(req)
            if data:
                value_array = data.get('value_array')
                if isinstance(value_array, list):
                    for i in value_array:
                        if isinstance(i.get('value'), (int, float)):
                            value += i.get('value')
                        else:
                            return jsonify(result="value类型错误")
                else:
                    return jsonify(result="value_array类型错误")
            return jsonify(result=value)
        except  Exception as e:
            print(e)


class Getdata(Resource):
    def get(self) -> json:
        return jsonify(date=time.strftime("%Y-%m-%d", time.localtime()))


class Chat(Resource):
    def post(self) -> json:
        try:
            req = request.get_data()
            data = json.loads(req)
            if data:
                msg = data.get('msg')
                if msg:
                    if "您好" in msg and "再见" in msg:
                        return jsonify(result="天气不错")
                    else:
                        if "您好" in msg:
                            return jsonify(result="您好，您吃了吗？")
                        elif "再见" in msg:
                            return jsonify(result="回见了您内。")
                        else:
                            return jsonify(result=" ")
                else:
                    return jsonify(result="获取msg错误")
            else:
                return jsonify(result="获取参数错误")

        except  Exception as e:
            print(e)


api.add_resource(Add, '/add')
api.add_resource(Getdata, '/get_date')
api.add_resource(Chat, '/chat')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3112)
