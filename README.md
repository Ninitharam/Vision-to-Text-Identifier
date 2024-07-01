# Vision-to-text-to-language-Identifier
To extract text from images and identify its language,offering an efficient solution for multilingual text recognition using NLP and image processing.

Focusing on Kannada and Marathi language currently.(IN PROGRESS)
## Background
In today's digital age, vast amounts of textual information are stored in image formats.
Extracting and interpreting this text is essential for various applications, from data retrieval
and accessibility to translation and content analysis. OCR (Optical Character Recognition)
technology enables the conversion of image-based text into machine-readable formats,
enhancing the usability and accessibility of digital content. By leveraging OCR and language
identification techniques, we can automate text extraction, streamline information retrieval,
and support multilingual communication across diverse fields.
## Motivation
The motivation for this project stems from the practical and far-reaching applications of OCR
(Optical Character Recognition) technology, aimed at addressing several key challenges and
opportunities:
• Efficient Information Retrieval: OCR technology enables the extraction of text from images,
allowing for efficient keyword searches, data mining, and content indexing. This capability is
vital for quickly locating specific information within large volumes of unstructured data.
• Multilingual Support: Images often contain text in multiple languages. By identifying the
language of the extracted text, we can facilitate accurate translation and comprehension,
thus supporting cross-lingual information retrieval and promoting global communication.
• Automation and Accuracy: Manual transcription of text from images is both time-
consuming and error-prone. OCR automates this process, significantly improving accuracy
and reducing the labour required for data entry and analysis.

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
