import os
import math
import random
import re
import sys

n=[29]

for number in n:
    print("")
    print(number)
    if number >= 1 and number<=100:
        if number % 2 == 0:
            if number >=2 and number <= 5:
                print("Not Weird")
            elif number >=6 and number <= 20:
                print("Weird")
            else:
                print("Not Weird")
        else:
            print("Weird")


#Problem: https://www.hackerrank.com/challenges/py-if-else/problem?h_r=next-challenge&h_v=zen