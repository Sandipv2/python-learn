from googletrans import Translator
from nltk.corpus import wordnet
import nltk

nltk.download("wordnet")

def get_definition(word):
    """Fetch English definitions using WordNet"""
    synsets = wordnet.synsets(word)
    if not synsets:
        return "❌ No definition found"
    # Return first meaning
    return synsets[0].definition()

def translate_word(word):
    translator = Translator()

    # Languages to translate into
    languages = {
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Hindi": "hi",
        "Japanese": "ja",
        "Russian": "ru"
    }

    # Print definition
    print(f"\n📖 English Definition of '{word}': {get_definition(word)}")

    print(f"\n🔹 Translations for '{word}':\n" + "-"*60)
    for lang, code in languages.items():
        try:
            translation = translator.translate(word, dest=code)
            print(f"{lang:10} → {translation.text}")
        except Exception:
            print(f"{lang:10} → ❌ Translation failed")

def main():
    print("=== 🌎 Vocabulary Translator ===")
    while True:
        word = input("\nEnter a word (or type 'exit' to quit): ").strip()
        if word.lower() == "exit":
            print("Thank you for using Vocabulary Translator! 👋")
            break
        translate_word(word)

if __name__ == "__main__":
    main()
