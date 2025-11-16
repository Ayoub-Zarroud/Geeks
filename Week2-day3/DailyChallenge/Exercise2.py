#pip install googletrans==4.0.0-rc1
from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translator = Translator()
translations = {}

for word in french_words:
    result = translator.translate(word, src='fr', dest='en')
    translations[word] = result.text  # Add translation to dictionary

print(translations)
