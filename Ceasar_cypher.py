
#"This is simple python code for Ceasar cypher encryption/decryption"

def caesar_cipher(text, shift, mode="encrypt"):
    """
    Encrypts or decrypts text using the Caesar Cipher method.

    Parameters:
    text (str): The input text (plaintext or ciphertext).
    shift (int): The shift value for the cipher.
    mode (str): "encrypt" to encrypt or "decrypt" to decrypt. Default is "encrypt".

    Returns:
    str: The resulting text after encryption or decryption.
    """
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    result = []
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(result)


#.....Main......
if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")




