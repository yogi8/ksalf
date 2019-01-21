from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
<<<<<<< HEAD
return ('Hello, World!')
=======
    return ('Hello, World!')
>>>>>>> d34230fc2b386830c9fc677a59a154b66b5af123
