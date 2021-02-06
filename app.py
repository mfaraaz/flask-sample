import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

from security import authenticate,identity

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='mfz'
api=Api(app)


jwt=JWT(app,authenticate,identity) #auth 

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/stores')
api.add_resource(StoreList,'/store/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=3000)