#!/usr/bin/env python3
def upcase_it():
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        args_upper = [arg.upper() for arg in args]
        print(" ".join(args_upper))
upcase_it()