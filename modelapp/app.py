from flask_restful import Resource, reqparse
class Item(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        data = Item.parser.parse_args()
        return data