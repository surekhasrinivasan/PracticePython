# Linear search

# Linear search

import sys
from cs50 import get_string

# Names in a phone book
book = [
    "Chen",
    "Kernighan",
    "Leitner",
    "Lewis",
    "Malan",
    "Muller",
    "Seltzer",
    "Shieber",
    "Smith"]

# Prompt user for name
name = get_string("name: ")
if name in book:
    print(f"Calling {name}")
