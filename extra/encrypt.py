# key = int(input("What key would you like to use?"))
# plain_text = str(input("What would you like to encrypt? "))

key = 3
plain_text = "Passwords are so secure when we use this encryption method"

LENGTH, UPPER_MIN, LOWER_MIN = 25, 65, 97


def get_next_character(character):
    if not character.isalpha():
        return character
    if character.isupper():
        min, max = UPPER_MIN, UPPER_MIN + LENGTH
    else:
        min, max = LOWER_MIN, LOWER_MIN + LENGTH
    # print("min / max values are:", min, "/", max)

    character_number = ord(character)

    # print("My character number is : ", character_number)
    # print(max)
    if character_number % max == 0:
        return chr(min)
    else:
        return chr(character_number + 1)



def encrypt(text):
    letter = "a"
    integer = 65
    character = chr(integer)
    print("Character ", integer, " is the letter ", character)
    ordinal_number = ord(letter)
    print("The Ordinal number for ", letter, " is ", ordinal_number)
    result = text
    for i in range(0, key):
        result = "".join([get_next_character(character) for character in result])
    return result


def decrypt(code):
    pass


encrypted_text = encrypt(plain_text)

print("Sorry I'm really bad at encryption.\n", "Your encrypted text is:", encrypted_text)
