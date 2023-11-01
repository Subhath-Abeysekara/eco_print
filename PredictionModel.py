import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

from upload_images import download_from_firebase

try:
    download_from_firebase('plant_type_and_week_model.h5')
    print("model_downloaded")
except:
    print("download error")
# Load the trained model
model = load_model('plant_type_and_week_model.h5')
plant_categories = ['Eggplant', 'Penaga_Laut', 'Terminalia_Catappa', 'Unknown']
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Unable to read image at {image_path}")
    img = cv2.resize(img, (128, 128))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(hsv)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = np.zeros_like(gray)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(contour_img, (x, y), (x + w, y + h), (255), -1)
    return np.stack([gray, hue, saturation], axis=-1), mask  # Using only 3 channels and returning the mask

def predict_and_display_features():
    img_features, mask = preprocess_image("uploaded.png")
    img_features = np.expand_dims(img_features, axis=0)

    green_percentage = np.sum(mask) / (128 * 128 * 255)
    if green_percentage < 0.05:
        return {
            "predicted_type": "Unknown",
            "Confidence": 0,
            "Week": 0
        }

    type_pred, week_pred = model.predict(img_features)
    predicted_type_index = np.argmax(type_pred)
    predicted_type = plant_categories[predicted_type_index]
    predicted_week = week_pred[0][0]
    predicted_week_rounded = round(predicted_week)
    confidence_score = type_pred[0][predicted_type_index] * 100

    # Check confidence
    if confidence_score < 70:
        return {
            "predicted_type": "Unknown",
            "Confidence": confidence_score,
            "Week": predicted_week_rounded
        }

    # Display the predictions and confidence score
    print(f"Predicted Plant Type: {predicted_type} (Confidence: {confidence_score:.2f}%)")
    print(f"Predicted Growth Stage (Week): {predicted_week_rounded}")

    return {
        "predicted_type":predicted_type,
        "Confidence":confidence_score,
        "Week":predicted_week_rounded
    }

# Test the function
# image_path = 'frame_327.jpg'
# predict_and_display_features(image_path)
