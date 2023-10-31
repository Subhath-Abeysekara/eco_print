from keras.models import load_model
from keras import preprocessing
import numpy as np
from keras.applications.resnet50 import preprocess_input
from upload_images import download_from_firebase

# Load the saved model
class_name= ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)__Common_rust',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape__Esca(Black_Measles)',
 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange__Haunglongbing(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,bell__Bacterial_spot',
 'Pepper,bell__healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
# Provide the path to the image you want to predict
try:
    download_from_firebase('model.h5')
    print("model_downloaded")
except:
    print("download error")
image_path = "uploaded.png"
loaded_model = load_model("model.h5")

def predict_disease():
    image = preprocessing.image.load_img(image_path, target_size=(256, 256))
    image = preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    predictions = loaded_model.predict(image)
    print(predictions)
    predicted_class_index = np.argmax(predictions)
    print(predicted_class_index)
    print(class_name[predicted_class_index])
    return {
        "disease":class_name[predicted_class_index]
    }