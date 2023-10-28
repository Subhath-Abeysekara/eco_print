from service import connect_images , connect_finetune
collection = connect_images()
collection2 = connect_finetune()

def upload_image(id , prediction , latitude, longitude):
    image_path = 'uploaded.png'
    with open(image_path, 'rb') as f:
        image_data = f.read()
    image_doc = {
        'user_id': id,
        'data': image_data,
        'hidden_state':False,
        'prediction':prediction,
        'latitude': latitude,
        'longitude': longitude
    }
    collection.insert_one(image_doc)
    del image_doc['user_id']
    collection2.insert_one(image_doc)

