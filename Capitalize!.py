#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    string = re.findall(r"^[a-z]|\s[a-z]", s)

    if len(string) != 0:
        if re.search("[^a-z]", string[0][0]) is None:

            s = re.sub(r"^[a-z]", string[0].upper(), s)
            del string[0]

    for i in string:
        i = i.split()
        if re.search("\d", i[0]) is None:

            h = re.search(r"^.+?\s[a-z]", s)
            index = h.span()[1]

            newStr = ""

            for j in range(len(s)):

                if j == index - 1:
                    newStr += s[j].upper()
                else:
                    newStr += s[j]
            s = newStr

    return s

s = input()
output = solve(s)
print(output)