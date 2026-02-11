#!/usr/bin/env python3
import sys
args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    num_list = []
    start = int(args[0])
    end = int(args[1])
    if start >= end:
        for i in list(range(start, end-1, -1)):
            num_list.append(i)
    else:
        for i in list(range(start, end+1)):
            num_list.append(i)
    print(num_list)