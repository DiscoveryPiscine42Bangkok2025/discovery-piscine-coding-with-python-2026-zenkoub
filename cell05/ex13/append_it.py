#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    for arg in args:
        if arg.endswith("ism"):
            pass
        else:
            print(arg + "ism")