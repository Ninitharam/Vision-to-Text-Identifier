# Vision-to-Text-Identifier
To extract text from images and identify its language,offering an efficient solution for multilingual text recognition using NLP and image processing.

Focusing on Kannada and Marathi language currently.(IN PROGRESS)

## Set Up Your Environment
- Download and install [Visual Studio Code](https://code.visualstudio.com/)

- Python Development Workload in Visual Studio: During the installation (or modification, if already installed) of Visual Studio, select the Python development workload. This includes the Python runtime and necessary tools to develop Python applications.
- Python Interpreter: While the Python development workload in Visual Studio typically installs a Python interpreter, you can also use an existing installation of Python on your system.

## Install Required Libraries
Install the necessary libraries using pip.
pip install opencv-python pytesseract langdetect

## Install Tesseract OCR
Windows: Download the installer from Tesseract at UB Mannheim and follow the installation instructions. Add Tesseract to your system PATH.
- [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

## Language Data Files
Tesseract requires language data files to recognize text in different languages. These data files are available separately and can be downloaded from the [Tesseract Language](https://github.com/tesseract-ocr/tessdata) Data repository on GitHub.

## Implement Language Detection for Text
Create a Python Script
Open VS Code, create a new file named language_recognition.py, and [add the following code to detect the language of a given text](https://github.com/Ninitharam/Vision-to-Text-Identifier/blob/e1685a374aebc60410a1ab65321d720d4ea8e902/language_recognition.py#L9).

## Implement Language Detection for Images

- Enhance the Script to Handle Images
Extend the [language_recognition.py script](https://github.com/Ninitharam/Vision-to-Text-Identifier/blob/c09114d43cada3b9b85bc97be87347dc78685bbe/language_recognition.py#L16) to include image processing using OpenCV and Tesseract OCR.

- Verify the Output
Ensure that the script correctly identifies the language for the image containing text.
