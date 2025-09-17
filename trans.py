from deep_translator import GoogleTranslator
from nltk.corpus import wordnet
import nltk

nltk.download("wordnet")

def get_definition(word):
    """Fetch English definitions using WordNet"""
    synsets = wordnet.synsets(word)
    if not synsets:
        return "❌ No definition found"
    return synsets[0].definition()

def translate_word(word):
    # Languages to translate into (Nepali at top)
    languages = {
        "Nepali": "ne",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Hindi": "hi",
        "Japanese": "ja",
        "Russian": "ru"
    }

    print(f"\n📖 English Definition of '{word}': {get_definition(word)}")
    print(f"\n🔹 Translations for '{word}':\n" + "-"*60)

    for lang, code in languages.items():
        try:
            translation = GoogleTranslator(source="en", target=code).translate(word)
            print(f"{lang:10} → {translation}")
        except Exception as e:
            print(f"{lang:10} → ❌ {e}")

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
