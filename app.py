from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resource.user import Register_newUser
from resource.items import Item, Items
from resource.store import Store,Stores

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "password"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items/')
api.add_resource(Stores, '/stores/')
api.add_resource(Register_newUser, '/register/')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(debug=True)
