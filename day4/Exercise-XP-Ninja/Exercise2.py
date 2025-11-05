# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse.split(' / ')
    decoded_words = []
    for word in words:
        decoded_chars = [reverse_dict.get(symbol, '') for symbol in word.split()]
        decoded_words.append(''.join(decoded_chars))
    return ' '.join(decoded_words)

# Example usage
english = "HELLO WORLD"
morse = text_to_morse(english)
print("Morse code:", morse)
print("Decoded text:", morse_to_text(morse))
