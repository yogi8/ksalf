from flask import Flask
from flask_restful import Api
from item import Item
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Item, '/item')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)