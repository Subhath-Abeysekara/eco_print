from service import connect_undefined
from upload_images import upload_image_to_firebase
collection = connect_undefined()

def upload_undefined(id , latitude, longitude , plant_name , plant_week):
    image_path = 'uploaded.png'
    image_doc = {
        'user_id': id,
        'data': upload_image_to_firebase(image_file=image_path),
        'hidden_state':False,
        'plant_week':plant_week,
        'plant_name':plant_name,
        'latitude':latitude,
        'longitude':longitude
    }
    collection.insert_one(image_doc)