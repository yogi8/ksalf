from flask_restful import Resource, reqparse
from flask import request
class Item(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        data = request.data['value']
        yogi =  {'yogi': data}
        return yogi