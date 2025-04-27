from PIL import Image

def jpg_to_pdf(jpg_path):
    pdf_path = jpg_path.replace('.jpg','.pdf')
    # Open the JPG image
    image = Image.open(jpg_path)
    
    # Convert to RGB if it's not because images in pdf must be in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Save as PDF
    image.save(pdf_path, 'PDF', resolution=100.0)
    print(f"Successfully converted {jpg_path} to {pdf_path}")


