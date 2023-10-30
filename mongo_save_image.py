from service import connect_images , connect_finetune
from upload_images import upload_image_to_firebase, get_sign_url_firebase

collection = connect_images()
collection2 = connect_finetune()

# def upload_image(id , prediction , latitude, longitude):
#     image_path = 'uploaded.png'
#     with open(image_path, 'rb') as f:
#         image_data = f.read()
#     image_doc = {
#         'user_id': id,
#         'data': image_data,
#         'hidden_state':False,
#         'prediction':prediction,
#         'latitude': latitude,
#         'longitude': longitude
#     }
#     collection.insert_one(image_doc)
#     del image_doc['user_id']
#     collection2.insert_one(image_doc)

def upload_image(id , prediction , latitude, longitude):
    image_path = 'uploaded.png'
    image_doc = {
        'user_id': id,
        'image': upload_image_to_firebase(image_file=image_path),
        'hidden_state':False,
        'prediction':prediction,
        'latitude': latitude,
        'longitude': longitude
    }
    collection.insert_one(image_doc)
    del image_doc['user_id']
    collection2.insert_one(image_doc)

def get_doc_image_url(document):
    document['image_url'] = get_sign_url_firebase(document['image'])
    del document['image']
    return document

def format_image_docs(documents):
    return list(map(lambda document: get_doc_image_url(document), documents))
