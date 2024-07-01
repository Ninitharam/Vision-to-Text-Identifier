import os
import cv2
import pytesseract
from langdetect import detect

# Set the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_language_text(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return str(e)

def detect_language_image(image_path):
    try:
        # Check if the file exists
        if not os.path.isfile(image_path):
            return f"File not found: {image_path}"

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Check if the image was successfully loaded
        if image is None:
            return f"Failed to load image: {image_path}"

        # Preprocess the image (convert to grayscale and apply thresholding)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(thresh)

        # Detect the language of the extracted text
        language = detect_language_text(extracted_text)
        return language
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # ENGLISH LANGUAGE
    sample_text = "This is an example text."
    print(f"Detected language (text): {detect_language_text(sample_text)}")

    # Use double backslashes or raw string for Windows file path
    image_path = r"C:\Users\NINITHA\Desktop\Swami-Vivekananda-suvichar-in-hindi-language-photos-.jpg.crdownload"
    print(f"Detected language (image): {detect_language_image(image_path)}")
