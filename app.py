from flask import Flask, jsonify

app = Flask(__name__)

stores = [
        {
            'name':'Book store',
            'Items':[
                    {
                    'Item':'Harry Potter',
                    'Price': 10.55
                    }
                    ]
        }
]

@app.route('/')
def home():
    return "Hello, World"

# POST / store data: {name}
@app.route('/store', methods = ['POST'])
def create_store():
    pass

# GET / store/<string:name>
@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
    pass

# GET / store
@app.route('/store', methods = ['GET'])
def get_stores():
    return jsonify({'stores': stores})

# POST / store/<string:name>/item {name,price}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    pass

# GET / store/<string:name>/item
@app.route('/store/<string:name>/item', methods = ['GET'])
def get_item_in_store(name):
    pass

app.run(port=5000)