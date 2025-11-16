import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        if count == 0:
            return f"'{word}' not found in text."
        return count

    def most_common_word(self):
        words = self.text.lower().split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        most_common = max(freq, key=freq.get)
        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        unique = set(words)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    def remove_stop_words(self):
        stop_words = {
            'a', 'an', 'the', 'and', 'or', 'is', 'are', 'was', 'were', 'in', 'on', 
            'at', 'to', 'for', 'of', 'with', 'as', 'by', 'from', 'that', 'this', 'it'
        }
        words = self.text.split()
        filtered = [w for w in words if w.lower() not in stop_words]
        self.text = " ".join(filtered)
        return self.text

    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return self.text

if __name__ == "__main__":
    sample_text = "Hello world! Hello universe. This is a test. Hello everyone!"
    t = Text(sample_text)
    print("Frequency of 'hello':", t.word_frequency("hello"))
    print("Most common word:", t.most_common_word())
    print("Unique words:", t.unique_words())

    text_from_file = Text.from_file("sample.txt")
    if text_from_file:
        print("Most common word in file:", text_from_file.most_common_word())

    tm = TextModification(sample_text)
    print("Remove punctuation:", tm.remove_punctuation())
    print("Remove stop words:", tm.remove_stop_words())
    print("Remove special characters:", tm.remove_special_characters())
