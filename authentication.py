import time
import jwt
import env
from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
from models.response import ErrorResponse


def generate_token_user(id,email, password , time_due):
    secret_key = env.SECRETE_KEY
    encoded_jwt = jwt.encode({"email": email,
                              "id":id,
                              "password": password,
                              "expire": int(time.time()) + time_due*60
                              }, secret_key,
                             algorithm="HS256")
    return encoded_jwt

def validate_token(request):
    try:
        token = request.headers.get('token')
    except:
        raise Exception(
            ErrorResponse(ResponseCode.MISSING_TOKEN, ResponseMessage.MISSING_TOKEN + str("errors")))
    secret_key = env.SECRETE_KEY
    decode = jwt.decode(token, secret_key,
                        algorithms=["HS256"])
    if decode['expire'] <= int(time.time()):
        raise Exception(
            ErrorResponse(ResponseCode.INVALID_AUTHENTICATION, ResponseMessage.INVALID_AUTHENTICATION + str("errors")))
    return decode['id']