#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str=str(number)
if number_str[-1]>5:
    print("Last digit of {} is {} and is greater than 5".format(number, number_str[-1]))
elif number_str[-1]==0:
    print("Last digit of {} is {} and is 0".format(number, number_str[-1]))
elif number_str[-1] < 6 and number_str[-1]!=0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, number_str[-1]))
