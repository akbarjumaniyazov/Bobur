from googletrans import Translator

def translate_text():
    translator = Translator()

    print("=== Tarjimon dasturi ===")
    text = input("Tarjima qilinadigan matnni kiriting: ")
    dest_lang = input("Qaysi tilga tarjima qilinsin? (masalan: en, ru, uz): ")

    try:
        translated = translator.translate(text, dest=dest_lang)
        print(f"\nTarjima: {translated.text}")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

if __name__ == "__main__":
    translate_text()
