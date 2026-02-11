#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    args_lower = [arg.lower() for arg in args]
    print(" ".join(args_lower))