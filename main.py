import string
import codecs

chars = string.ascii_lowercase

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.',
        '--.', '....', '..', '.---', '-.-', '.-..',
        '--', '-.', '---', '.--.', '--.-', '.-.',
        '...', '-', '..-', '...-', '.--', '-..-',
        '-.--', '--..', '.----', '..---', '...--',
        '....-', '.....', '-....', '--...', '---..',
        '----.', '-----', '--..--', '.-.-.-', '..--..',
        '-..-.', '-....-', '-.--.', '-.--.-']

morse_char_index = list(string.ascii_uppercase) + list(string.digits)[1:len(string.digits)] + ['0',',','.','?','/','-','(',')']

print("SimpleKey v1.0.0")

while True:
    try:
        print("\n")
        print("1. Caeser Cipher")
        print("2. ROT13")
        print("3. Morse Code")
        print("0. Quit")
        selection = input("Enter a selection: ")

        if selection == "0" or selection.lower() == "quit":
            break

        raw = input("Enter encrypted string: ")

        if selection == "1" or selection.lower() == "caeser" or selection.lower() == "caeser cipher":
            for i in range(26):
                dest = chars[i:] + chars[:i]
                decoded = ''.join(dest[chars.index(raw_char)] for raw_char in raw)
                print("Shift +"+str(i)+":"+" "+decoded.upper())

        if selection == "2" or selection.lower() == "rot13":
            print(codecs.decode(raw, "rot_13"))

        if selection == "3" or selection.lower() == "morse" or selection.lower() == "morse code":
            raw_array = raw.split(" ")
            decoded = ""
            for e in raw_array:
                for i in range(len(morse)):
                    if e == morse[i]:
                        decoded += morse_char_index[i]
            print(decoded)

    except ValueError:
        print("Special characters are not supported.")


