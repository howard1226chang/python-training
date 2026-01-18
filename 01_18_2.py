def Area_cal(n, s):
    Area = (n*(s*s)/(4*tan(math.pi/n)))
    #A = n*s*s
    return Area

import math
from math import pow, tan
n,s = input('輸入正n邊形和邊長s:').split(" ")
n=int(n)
s=float(s)
result = Area_cal(n,s)
print("%.4f"% result)