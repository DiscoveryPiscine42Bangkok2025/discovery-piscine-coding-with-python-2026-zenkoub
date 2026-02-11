#!/usr/bin/env python3
import sys
keyword = sys.argv[1]
text = input("What was the parameter? ")
if keyword == text:
    print("Good job!")
else:
    print("Nope, sorry...")