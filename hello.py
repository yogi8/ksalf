from flask import Flask,jsonify,request
app = Flask(__name__)

stores = [
           {'name': 'MyStore',
            'items': [
                      {'name': 'my item','price': 15.99}
                     ]
           }
          ]
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store' , methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})



if __name__ == '__main__':
 app.run(host='0.0.0.0',port=5000, debug=True)