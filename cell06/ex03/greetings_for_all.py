#!/usr/bin/env python3
def greetings(names="noble stranger"):
    if not isinstance(names, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {names}.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)