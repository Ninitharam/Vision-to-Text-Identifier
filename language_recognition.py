import os
import cv2
import pytesseract
from langdetect import detect

# Set TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = 'C:\\Program Files\\Tesseract-OCR\\'  # Adjust this path as per your installation

def detect_language_text(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return str(e)

def detect_language_image(image_path):
    try:
        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Preprocess the image (convert to grayscale and apply thresholding)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(thresh, lang='kan')

        # Detect the language of the extracted text
        language = detect_language_text(extracted_text)
        return language
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    sample_text = "This is an example text."
    print(f"Detected language (text): {detect_language_text(sample_text)}")

    image_path =  "C:\\Users\\NINITHA\\OneDrive\\Documents\\Python Scripts\\download.png"
    print(f"Detected language (image): {detect_language_image(image_path)}")
