from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# "C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_screenshot(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Use Tesseract to perform OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage
screenshot_path = 'C:\\Users\Ramir\\Documents\\ScreenText Translator\\screenshot.png'
#"C:\Users\Ramir\OneDrive\Documents\test.png"
#"C:\Users\Ramir\Documents\ScreenText Translator\screenshot.png"
extracted_text = extract_text_from_screenshot(screenshot_path)

print("Extracted Text:")
print(extracted_text)