from flask_restful import Resource, reqparse
from flask import request
import json
class Item(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        data = json.loads(request.data)
        ac = int(data['enterprises_details'][0]['enterpriseBranchId'])
        ad = data['enterprises_details']
        ae = data['admin_details']
        af = data['gateways']
        ag = data['bandwidth_rules']
        return ac