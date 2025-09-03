import sys
import math

input = sys.argv
# input example 5,2 4,5
x1,y1 = input[1].split(',')
x2,y2 = input[2].split(',')

print(input)
print(f"x1: {x1}\ny1: {y1}\nx2: {x2}\ny2: {y2}")

def dist_func(x1,y1,x2,y2):
    dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
    print(f"distance: {dist}")

if len(input) == 5:
    dist_func(x1,y1,x2,y2)