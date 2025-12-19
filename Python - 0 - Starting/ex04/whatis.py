import sys

if len(sys.argv) == 1:
    sys.exit()

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        num = int(sys.argv[1])
        
        if num % 2 == 0:
            print("I\'m Even.")
        else:
            print("I\'m Odd.")

    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as err:
    print(f"AssertionError: {err}")
    sys.exit(1)