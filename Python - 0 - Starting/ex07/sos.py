import sys


def main():
    """
    Encode a string into Morse code
    """
    nested_morse = {
        " ": "/",
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....",
        "7": "--...", "8": "---..", "9": "----.",
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        input_str = sys.argv[1]
        result = []

        for char in input_str.upper():
            if char in nested_morse:
                result.append(nested_morse[char])
            else:
                raise AssertionError("the arguments are bad")

        print(" ".join(result))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
