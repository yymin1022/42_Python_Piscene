"""
Exercise 05: building.py
Count characters in a string (upper, lower, punctuation, space, digit).
"""
import string
import sys


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
    except AssertionError as err:
        print(f'AssertionError: {err}')


if __name__ == "__main__":
    main()
