from flask_restful import Resource, reqparse
from flask import request
import json
class Item(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        data = json.loads(request.data)
        ac = int(data['enterprises_details'][0]['enterpriseBranchId'])
        return ac