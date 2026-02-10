#!/usr/bin/env python3
import sys
args = sys.argv[1:]

if len(args) == 0:
    numbers = range(0, 11)
else:
    try:
        numbers = [int(x) for x in args]
    except ValueError:
        print("none")
        sys.exit()

for n in numbers:
    print(f"Table de {n}:", end=" ")
    for i in range(0, 11):
        print(n * i, end=" ")
    print()
