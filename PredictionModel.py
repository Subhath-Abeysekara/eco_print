import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

# Load the trained model
model = load_model('plant_type_and_week_model.h5')
plant_categories = ['Eggplant', 'Penaga_Laut', 'Terminalia_Catappa', 'Plant Unknown']

def display_image_features(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(hsv)

    # Detect contours and compute their height
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = np.zeros_like(gray)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(contour_img, (x, y), (x + w, y + h), (255), 2)

    # Display the images
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs[0, 0].imshow(gray, cmap='gray')
    axs[0, 0].set_title('Grayscale')
    axs[0, 1].imshow(hue, cmap='gray')
    axs[0, 1].set_title('Hue')
    axs[0, 2].imshow(saturation, cmap='gray')
    axs[0, 2].set_title('Saturation')
    axs[1, 0].imshow(value, cmap='gray')
    axs[1, 0].set_title('Value')
    axs[1, 1].imshow(contour_img, cmap='gray')
    axs[1, 1].set_title('Contours')
    for ax in axs.ravel():
        ax.axis('off')
    plt.tight_layout()
    # plt.show()

def predict_and_display_features():
    # Load and preprocess the image
    image_path = "uploaded.png"
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (128, 128))  # Resize to 128x128 pixels

    # Display image features
    display_image_features(img_resized)

    # Add a batch dimension for prediction
    img_batch = np.expand_dims(img_resized, axis=0)

    # Make predictions
    type_pred, week_pred = model.predict(img_batch)

    # Get the predicted plant type and week
    predicted_type_index = np.argmax(type_pred)
    predicted_type = plant_categories[predicted_type_index]
    predicted_week = week_pred[0][0]  # Extract the week value from the 2D array

    # Round the predicted week to the nearest whole number
    predicted_week_rounded = round(predicted_week)

    # Get the confidence score for the plant type prediction
    confidence_score = type_pred[0][predicted_type_index] * 100  # Convert to percentage

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
