#!/usr/bin/env python3
user_input = float(input("Give me a number: "))
if user_input % 1 == 0:
    print(f"This number is an integer.")
else:
    print(f"This number is a decimal.")