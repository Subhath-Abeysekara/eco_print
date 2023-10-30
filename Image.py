from bson import ObjectId
from common import format_docs
from models.response import ErrorResponse, SuccessResponse
from mongo_save_image import format_image_docs
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
        images_ = format_image_docs(images)
        response = {
            "images" :format_docs(images_)
        }
        return SuccessResponse(response).generate()
    except:
        raise Exception(
            ErrorResponse(15,str("error")))

def get_unhidden_images(id):
    try:
        print(id)
        images = collection.find({'hidden_state':False,'user_id':id})
        images_ = format_image_docs(images)
        response = {
            "images": format_docs(images_)
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