from service import connect_user
from schemas import User , Login
from validate_inputs import validate_inputs
from models.response import SuccessResponse, ErrorResponse, Response
from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
from authentication import generate_token_user
collection = connect_user()

def register_user(user):
    schema = User(many=False)
    validate_inputs(body=user, schema=schema)
    users = collection.find({'email':user['email']})
    if list(users) != []:
        raise Exception(
            ErrorResponse(ResponseCode.EMAIL_EXIST, ResponseMessage.EMAIL_EXIST + str("errors")))
    collection.insert_one(user)
    response = {
        'message': "success",
    }
    return SuccessResponse(response).generate()

def login_user(user):
    schema = Login(many=False)
    validate_inputs(body=user, schema=schema)
    user = collection.find({'email':user['email'],'password':user['password']})
    if list(user) == []:
        raise Exception(
            ErrorResponse(ResponseCode.NOT_REGISTER, ResponseMessage.NOT_REGISTER + str("errors")))
    token = generate_token_user(id=str(user[0]['_id']),email= user['email'] ,password= user['password'] ,time_due= 8600)
    response = {
        "token" : token
    }
    return SuccessResponse(response).generate()