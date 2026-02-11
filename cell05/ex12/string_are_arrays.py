#!/usr/bin/env python3
import sys
input = sys.argv[1]
count = input.count('z')
if count == 0:
    print('none')
elif len(sys.argv) != 2:
    print('none')
else:
    print('z' * count)