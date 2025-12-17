"""
Exercise 05: building.py
Count characters in a string
(upper, lower, punctuation, space, digit).
"""
import string
import sys


def analyze_text(text: string):
    """
    Count characters in text from parameter
    (upper, lower, punctuation, space, digit)
    """
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main function of building.py
    """
    try:
        args = sys.argv
        text = None

        if len(args) > 2:
            raise AssertionError('too many arguments')
        elif len(args) == 2:
            text = args[1]
        else:
            print("What is the text to count?")
            try:
                text = sys.stdin.readline()
                if not text:
                    pass
            except KeyboardInterrupt:
                pass

        analyze_text(text)
    except AssertionError as err:
        print(f'AssertionError: {err}')


if __name__ == "__main__":
    main()
