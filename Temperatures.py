#https://www.codingame.com/ide/puzzle/temperatures Filip Wrzesień s16720

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
result = ''

if len(temps) == 0:
    print("0")
else:
    temps_split = temps.split()
    result = temps_split[0]

    for temp in temps_split:
        if abs(int(temp)) < abs(int(result)):
            result = temp
        elif abs(int(temp)) == abs(int(result)):
            result = max(int(temp),int(result))

print(result)
