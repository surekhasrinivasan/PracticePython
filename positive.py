# Print a positive integer
from cs50 import get_int

"""def main():
    i = get_positive_int("Positive integer, please: ")
    print(i)

def get_positive_int(prompt):
    while True:
        n = get_int(prompt)
        if n >= 1:
            break
    return n

if __name__ == "__main__":
    main()"""

i = get_positive_int("Positive integer, please: ")
print(i)

def get_positive_int(prompt):
    while True:
        n = get_int(prompt)
        if n >= 1:
            break
    return n