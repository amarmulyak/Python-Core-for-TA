a = 0.1
b = 0.8
h = 0.01

x = 0.5

import math
while x <=b:
    si = 1
    s = 0
    k = 1
    while si > 10 ** (-5):
        si = k * (k + 1) * (x ** k)
        #print(si)
        s+=si
        k+=1
    y = 2*x/((1-x)**3)
    p = math.fabs((s-y)/y)*100
    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x+=h