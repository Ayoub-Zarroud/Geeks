# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # only shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # keep spaces/punctuation unchanged
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


# Main program
print("=== Caesar Cipher ===")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift value (e.g., 3): "))

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("\nEncrypted message:", encrypted)
elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("\nDecrypted message:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
