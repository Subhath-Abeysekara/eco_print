from bson import ObjectId
from common import format_docs
from models.response import ErrorResponse, SuccessResponse
from service import connect_images

collection = connect_images()

def check_user_id(collection_name,doc_id,id):
    document = collection_name.find_one({'_id':ObjectId(doc_id)})
    if document['user_id']!=id:
        raise Exception(
            ErrorResponse(15, str("error id")))

def hide_image(image_id,id):
    try:
        check_user_id(collection_name=collection , doc_id=image_id , id=id)
        collection.update_one({'_id':ObjectId(image_id)},{'$set':{'hidden_state':True}})
        response = {
            "message" : "success"
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error id")))

def unhide_image(image_id,id):
    try:
        check_user_id(collection_name=collection , doc_id=image_id , id=id)
        collection.update_one({'_id':ObjectId(image_id)},{'$set':{'hidden_state':False}})
        response = {
            "message" : "success"
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error id")))

def get_all_images():
    try:
        images = collection.find({'hidden_state':False})
        response = {
            "images" :format_docs(images)
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error id")))

def get_hidden_images(id):
    try:
        images = collection.find({'hidden_state':False,'user_id':id})
        response = {
            "images" :format_docs(images)
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error id")))

def delete_image(image_id,id):
    try:
        check_user_id(collection_name=collection, doc_id=image_id, id=id)
        collection.update_one({'_id':ObjectId(image_id)},{'$set':{'hidden_state':True}})
        response = {
            "message" : "success"
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error id")))