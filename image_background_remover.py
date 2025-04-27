from rembg import remove
from PIL import Image
import io

def remove_background(input_path):

    if '.jpg' in input_path:
        output_path = input_path.replace('.jpg', '.png')
    elif '.jpeg' in input_path:
        output_path = input_path.replace('.jpeg', '.png')
    else:
        output_path = input_path
    # Open the input image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    # Remove background
    output_data = remove(input_data)

    # Save the result
    output_image = Image.open(io.BytesIO(output_data))
    output_image.save(output_path)
    print(f"Background removed and saved to {output_path}")

