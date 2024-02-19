import shutil
import os

def move_tesseract_to_program_files():
    # Define source and destination paths
    tesseract_source_path = r'E:\Tesseract-OCR\tesseract.exe'
    #"E:\Tesseract-OCR\tesseract.exe"
    program_files_destination = os.path.join(os.environ["ProgramFiles"], "Tesseract-OCR")

    # Check if the source directory exists
    if not os.path.exists(tesseract_source_path):
        print("Tesseract-OCR directory not found.")
        return

    # Check if the destination directory already exists
    if os.path.exists(program_files_destination):
        print("Tesseract-OCR is already in Program Files.")
        return

    try:
        # Move the directory
        shutil.move(tesseract_source_path, program_files_destination)
        print("Tesseract-OCR moved to Program Files successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    move_tesseract_to_program_files()
