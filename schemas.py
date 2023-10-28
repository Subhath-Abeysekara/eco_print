from marshmallow import Schema, fields , validate

class User(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    city = fields.Str(required=True)
    email = fields.Str(required=True)
    occupation = fields.Str(required=True)
    password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)

class Login(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)



