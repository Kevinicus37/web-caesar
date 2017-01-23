def alphabet_position(letter):
    '''Returns ordinance of the supplied letter - normalized to lower case'''

    return ord(letter.lower())

def rotate_character(char, rot):
    '''Returns encypted character equivalent of supplied character based on the
   rotation value given'''

   # If the supplied character is not alpha, the character is not returned
   # without encryption.

    if not char.isalpha():
        return char

    pos = alphabet_position(char)

    # Find encrypted character based on the difference of the ordinal value of
    # the character plus rotation and the ordinal value of 'a'.  Modulus of the
    # number of characters in the alphabet (26) is applied and finally the
    # ordinal of 'a' is added back.  The character of this value is returned
    # upper case if the original character was also uppercase, and lowercase
    # otherwise.

    if char.isupper():
        return chr(((pos - ord('a') + rot) % 26)+ ord('a')).upper()
    else:
        return chr(((pos - ord('a') + rot) % 26)+ ord('a'))

def encrypt(text, rot):
    '''Receives a string and changes each character by rotating its position
       in the alphabet by rot amount and returns an encrypted string'''

    newStr = ""
    for char in text:
        newStr += rotate_character(char, rot)
    return newStr
