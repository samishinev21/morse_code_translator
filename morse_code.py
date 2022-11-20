DICTIONARY = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-","L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....","7": "--...", "8": "---..", "9": "----."}

def from_english_to_morse(text):
    letters = list(text)
    result = []
    for letter in letters:
        result.append(DICTIONARY[letter])
    
    return result

morse_code = from_english_to_morse("HI IM SAMUEL")
print(" ".join(morse_code))