import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Price is required!")
    parser.add_argument('store_id', type=int, required=True, help="Store ID is required!")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":f"{name!r} not found!"}

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": f"{name!r} is exists"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "Internal server error!"}, 500
        return {"message": f"{name!r} inserted"}, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": f"Item {name!r} Deleted"}
        return {"message":f"{name!r} not found!"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)
        item.save_to_db()
        return item.json()


class Items(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
