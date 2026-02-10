#!/usr/bin/env python3
user_input = int(input("Enter a number\n"))
for i in range(1, 10):
    multiplication = user_input * i
    print(f"{i} x {user_input} = {multiplication}")
