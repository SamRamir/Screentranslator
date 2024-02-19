# ScreenTranslator

ScreenTranslator is a Python application that allows you to select a portion of the screen and translates the text within it from English to Spanish.

## Features

- Capture a portion of the screen to translate.
- Uses Tesseract OCR for text extraction.
- Utilizes Google Translate API for translation.
- Simple GUI built with Tkinter.

## Installation

1. Download the `ScreenTranslatorApp.exe` file.
2. Install Tesseract-OCR by placing the Tesseract-OCR folder into `C:\Program Files\`.
    - You can download Tesseract-OCR from its [GitHub repository](https://github.com/tesseract-ocr/tesseract).
    - Follow the installation instructions provided in the repository.
3. Run `ScreenTranslatorApp.exe`.


## Usage

1. Launch the application by running `ScreenTranslatorApp.exe`.
2. Click on "Iniciar Captura" to start capturing the screen.
3. Click and drag to select the area of the screen you want to translate.
4. Release the mouse button to capture the selected area.
5. The extracted text will be translated from English to Spanish.
6. View the translated text in a separate window.
7. Close the application when done.

## Dependencies

- `tkinter` - Python's standard GUI (Graphical User Interface) package.
- `pyautogui` - Python module for controlling the mouse and keyboard.
- `pytesseract` - Python wrapper for Google's Tesseract-OCR Engine.
- `PIL` (Python Imaging Library) - Python imaging library to work with images.
- `googletrans` - Python module for Google Translate API.

## Notes

- Ensure proper installation of Tesseract-OCR for text extraction to work correctly.
- Internet connection is required for translation using Google Translate API.

## License

