import sys
from ft_filter import ft_filter


def main():
    """
    Function to filter words from a string by length.
    Accepts two arguments: a string (S) and an integer (N).
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]

        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = s.split()
        result = [word for word in ft_filter(lambda x: len(x) > n, words)]

        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
