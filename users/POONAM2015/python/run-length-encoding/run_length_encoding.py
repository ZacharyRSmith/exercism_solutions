"""Exercism run_length_encoding problem"""
def decode(string: str) -> str:
    decoded_text = ''
    number = ''
    for c in string:
        if c.isdigit():
            number += c
        else:
            if number:
                decoded_text += str(int(number) * c)
                number = ''
            else:
                decoded_text += c
    return decoded_text


def encode(string: str) -> str:
    encoded_text = ''
    if string == '':
        return encoded_text
    count = 0
    character = string[0]
    for c in string:
        if c == character:
            count += 1
        else:
            if count == 1:
                encoded_text += character
            else:  # count > 1
                encoded_text += str(count) + character
            character = c
            count = 1
    encoded_text += str(count) + character  \
        if count > 1  \
        else character
    return encoded_text
