alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cypher(text, shift=0):
    pass


def encrypt(text, shift=0):

    new_text = ""

    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter.lower())
            new_letter = alphabet[(index + shift) % len(alphabet)]
            new_text += new_letter
        else:
            new_text += letter


    return new_text

def decrypt(text, shift=0):
    new_text = ""

    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter.lower())
            new_letter = alphabet[(index - shift) % len(alphabet)]
            new_text += new_letter
        else:
            new_text += letter

    return new_text

shift_amount = 100

encrypted_text = encrypt("some string that i want encrypted", shift_amount)
decrypted_text = decrypt(encrypted_text, shift_amount)
print(encrypted_text,   "\n", decrypted_text)
