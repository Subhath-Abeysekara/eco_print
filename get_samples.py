from upload_images import get_sign_url_firebase, get_sign_url_firebase_sample
def get_two_samples(prediction):
    file_name1 = f"{prediction['predicted_type']}_Week {str(prediction['Week'])}_Sample1.jpg"
    file_name2 = f"{prediction['predicted_type']}_Week {str(prediction['Week'])}_Sample2.jpg"
    url1 = get_sign_url_firebase_sample(file_name=file_name1)
    url2 = get_sign_url_firebase_sample(file_name=file_name2)
    res = {
        "image1":url1,
        "image2":url2
    }
    print(res)
    return res