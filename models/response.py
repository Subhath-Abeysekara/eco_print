import  json

RESPONSE_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*', # Required for CORS support to work
    'Access-Control-Allow-Credentials': True, # Required for cookies, authorization headers with HTTPS
}

class Response:
    def __init__(self,state, data = {}, status_code = 400, code  = -1,  response_message = ''):
        self.body = {
            'state':state,
            'data': data,
            'code': code,
            'message': response_message
        }
        self.status_code = status_code

    def generate(self):
        return {
            'statusCode': self.status_code,
            'body': self.body
        }

class SuccessResponse(Response):
    def __init__(self, data):
        super().__init__(True,data,200,0,'success')

class SuccessMessageResponse(Response):
    def __init__(self, message):
        super().__init__(True,{'info':message},200,0,'success')


class ErrorResponse(Response,Exception):
    def __init__(self, response_code,response_message):
        super().__init__(False,{},400,response_code,response_message)