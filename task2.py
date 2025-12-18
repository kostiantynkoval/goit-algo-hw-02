from collections import deque
from sys import argv


def main():
    try:
        d = deque("".join(argv[1:]).lower().strip())
        print(d)
        while len(d) > 1:
            left = d.popleft()
            right = d.pop()
            if left != right:
                print("The string is not a palindrome.")
                return
        print("The string is a palindrome.")

    except IndexError:
        print("Please provide a string as a command-line argument.")


if __name__ == '__main__':
    main()

