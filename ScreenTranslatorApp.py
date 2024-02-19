import tkinter as tk
import pyautogui
import pytesseract
from PIL import Image, ImageTk
from translate import Translator

class ScreenshotApp:
    def __init__(self, root):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.root = root
        self.root.title("Traductor de Capturas de Pantalla")
        self.transparent = False

        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button = tk.Button(root, text="Iniciar Captura", command=self.start_screenshot)
        self.button.pack()

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.root.winfo_pointerx()
        self.start_y = self.root.winfo_pointery()

    def on_drag(self, event):
        self.end_x = self.root.winfo_pointerx()
        self.end_y = self.root.winfo_pointery()

        self.canvas.delete("rect")
        self.canvas.create_rectangle(
            self.start_x, self.start_y, self.end_x, self.end_y, outline="red", tags="rect"
        )

    def on_release(self, event):
        min_x = min(self.start_x, self.end_x)
        min_y = min(self.start_y, self.end_y)
        width = abs(self.end_x - self.start_x)
        height = abs(self.end_y - self.start_y)

        screenshot = pyautogui.screenshot(region=(min_x, min_y, width, height))
        screenshot.save("screenshot.png")

        text = self.extract_text("screenshot.png")
        translated_text = self.translate_text(text, 'en', 'es')
        self.show_text_window(translated_text)

    def extract_text(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

    def translate_text(self, text, src_lang, dest_lang):
        translator = Translator(to_lang=dest_lang)
        translation = translator.translate(text)
        return translation

    def show_text_window(self, text):
        text_window = tk.Toplevel(self.root)
        text_window.title("Texto Extraído")

        text_label = tk.Label(text_window, text=text, font=("Arial", 12), wraplength=500, justify="left")
        text_label.pack(padx=20, pady=20)

        new_screenshot_button = tk.Button(text_window, text="Nueva Captura", command=lambda: self.new_screenshot(text_window))
        new_screenshot_button.pack(pady=10)

        close_button = tk.Button(text_window, text="Cerrar", command=self.close_app)
        close_button.pack(pady=10)

    def new_screenshot(self, text_window):
        text_window.destroy()
        self.root.attributes("-fullscreen", False)
        self.root.attributes("-alpha", 1.0)
        self.transparent = False
        self.button.config(state=tk.NORMAL)  # Enable the button

    def close_app(self):
        self.root.destroy()

    def start_screenshot(self):
        if not self.transparent:
            self.root.attributes("-fullscreen", True)
            self.root.attributes("-alpha", 0.5)
            self.transparent = True
            self.button.config(state=tk.DISABLED)  # Disable the button
        else:
            self.root.attributes("-fullscreen", False)
            self.root.attributes("-alpha", 1.0)
            self.transparent = False
            self.button.config(state=tk.NORMAL)  # Enable the button

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
