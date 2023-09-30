import math
ab=int(input())
bc=int(input())

tanx=ab/bc
print(f'{round(math.degrees(math.atan(tanx)))}'+'\u00b0')