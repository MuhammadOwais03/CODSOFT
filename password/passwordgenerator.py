import secrets


def GeneratePassword(length):
    digits = '0123456789'
    UpperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    specialCharacter = '!@#$%'
    LowerLetters = UpperLetters.lower()
    collection_of_alphabets_and_digits = digits+UpperLetters+LowerLetters+specialCharacter
    password = ''.join((secrets.choice(collection_of_alphabets_and_digits) for i in range(length)))
    return password

if __name__ == "__main__":

    length = int(input('Enter Length For The Password: '))
    password = GeneratePassword(length)
    print("Generated Password: ",password)
    input()
