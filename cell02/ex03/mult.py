#!/usr/bin/env python3
first_num = int(input("Enter first number:\n"))
second_num = int(input("Enter second number:\n"))
multiplication = first_num * second_num
print(first_num, " x ", second_num, " = ", multiplication)
if multiplication < 0:
    print("The result is negative.")
elif multiplication == 0:   
    print("The result is positive and negative.")
else:
    print("The result is positive.")