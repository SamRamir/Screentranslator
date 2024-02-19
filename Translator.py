from googletrans import Translator

def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, dest='es')
    return translation.text

# Example
english_text = "Hello, how are you?"
spanish_translation = translate_to_spanish(english_text)
print(f"English: {english_text}")
print(f"Spanish: {spanish_translation}")