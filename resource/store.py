from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": f"cannot find {name!r}."}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"{name!r} is available"}

        try:
            store = StoreModel(name)
            store.save_to_db()
        except:
            return {"message": "Internal Error"}, 500
        return {"message": f"{name} store created"}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": f"{name} deleted"}


class Stores(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
