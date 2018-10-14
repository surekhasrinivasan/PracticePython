# Prints the initials of the name specified by user

from cs50 import get_string

s = get_string("name: ")
initials = ""
for c in s:
    if c.isupper():
        initials += c
print(initials)