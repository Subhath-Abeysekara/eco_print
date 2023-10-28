from flask import Flask,request, jsonify
from flask_cors import CORS , cross_origin

from Image import hide_image, get_all_images, unhide_image
from PredictionModel import predict_and_display_features
from User import register_user , login_user
from authentication import validate_token
from instructions import get_instruction
from mongo_save_image import upload_image
from undefined_image_add import upload_undefined

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

@app.route("/")
def main():
    return "hello world"

@app.route("/home")
@cross_origin()
def home():
    return "First Page"

@app.route("/v1/register" , methods=["POST"])
@cross_origin()
def register():
    return register_user(request.json())

@app.route("/v1/login" , methods=["POST"])
@cross_origin()
def login():
    return login_user(request.json())

@app.route("/v1/upload", methods=["POST"])
@cross_origin()
def image_upload():
    print("main")
    id = validate_token(request=request)
    uploaded_file = request.files['image']
    latitude = request.files['latitude']
    longitude = request.files['longitude']
    if uploaded_file:
        uploaded_file.save('uploaded.png')
        prediction = predict_and_display_features()
        upload_image(id=id , prediction=prediction,longitude=longitude,latitude=latitude)
        return prediction

@app.route("/v1/undefinedimage", methods=["POST"])
@cross_origin()
def image_upload_undefined():
    print("main")
    id = validate_token(request=request)
    uploaded_file = request.files['image']
    latitude = request.files['latitude']
    longitude = request.files['longitude']
    plant_name = request.files['plant_name']
    plant_week = request.files['plant_week']
    if uploaded_file:
        uploaded_file.save('uploaded.png')
        upload_undefined(id=id,longitude=longitude,latitude=latitude,plant_name=plant_name,plant_week=plant_week)
        return {
            "message":"success"
        }

@app.route("/v1/hide/<image_id>", methods=["PUT"])
@cross_origin()
def hide_image(image_id):
    id = validate_token(request=request)
    return hide_image(image_id=image_id,id=id)

@app.route("/v1/unhide/<image_id>", methods=["PUT"])
@cross_origin()
def unhideimage(image_id):
    id = validate_token(request=request)
    return unhide_image(image_id=image_id,id=id)

@app.route("/v1/images")
@cross_origin()
def get_images():
    id = validate_token(request=request)
    return get_all_images()

@app.route("/v1/user/hidden_images")
@cross_origin()
def get_hidden_images():
    id = validate_token(request=request)
    return get_hidden_images(id=id)

@app.route("/v1/instructions")
@cross_origin()
def get_instructions():
    id = validate_token(request=request)
    return get_instruction()

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)

