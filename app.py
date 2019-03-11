import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
    port=int(os.getenv('PORT', '5000')),
    debug=True)