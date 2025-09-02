import sys
import math

input = sys.argv

print(input)
x1,y1 = input[1].split(',')
x2,y2 = input[2].split(',')
print(f"x1: {x1}\ny1: {y1}\nx2: {x2}\ny2: {y2}")

dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
print(f"distance: {dist}")