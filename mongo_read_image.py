from PIL import Image
import io

from service import connect_images
collection = connect_images()

target_filename = 'your_image.jpg'
result = collection.find_one({'filename': target_filename})
if result:
    image_data = result['data']
    image = Image.open(io.BytesIO(image_data))
    image.show()
else:
    print(f"Image with filename '{target_filename}' not found.")