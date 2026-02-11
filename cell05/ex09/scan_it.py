#!/usr/bin/env python3
import sys
import re
if len(sys.argv) < 2:
    print("none")
else:
    kword = sys.argv[1]
    match = re.findall(kword, sys.argv[2])
    print(len(match))