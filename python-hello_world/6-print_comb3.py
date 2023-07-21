#!/usr/bin/python3
combinations = []
for y in range(10):
    for x in range(y+1, 10):
        combinations.append("{:02d}".format(y * 10 + x))

print(", ".join(combinations))
 
