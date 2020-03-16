import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class Register_newUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username is Required!")
    parser.add_argument("password", type=str, required=True, help="Password is Required!")

    def post(self):
        data = Register_newUser.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists."}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "New User Registered Successfully!"}, 201
