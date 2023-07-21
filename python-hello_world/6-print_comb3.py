#!/usr/bin/python3
for y in range(10):
    for x in range(y + 1, 10):
        print("{:02d}".format(y * 10 + x), end=', ' if x < 9 else ' ') 
