from service import connect_undefined
collection = connect_undefined()

def upload_undefined(id , latitude, longitude , plant_name , plant_week):
    image_path = 'uploaded.png'
    with open(image_path, 'rb') as f:
        image_data = f.read()
    image_doc = {
        'user_id': id,
        'data': image_data,
        'hidden_state':False,
        'plant_week':plant_week,
        'plant_name':plant_name,
        'latitude':latitude,
        'longitude':longitude
    }
    collection.insert_one(image_doc)