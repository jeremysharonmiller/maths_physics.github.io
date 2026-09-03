# Stitson p.164
# Rotman p.47

import math as m

# Input a and b 
a = 289
b = 51

r = [0]*100
q = [0]*100

n = 1

r[0] = abs(a)  #r0
r[1] = abs(b)  #r1

while r[n] !=  0:
    q[n]     = r[n-1] // r[n] 
    r[n + 1] = r[n-1] - q[n]*r[n]
    n        = n+1

n = n-1
d = r[n]
    
print( "gcd(%d,%d)=%d"% (a,b,d))

test = d==m.gcd(a,b);

print( "\nTest d = gcd(a,b):\n")

print( "%d == gcd(%d,%d), %s\n\n"% (d,a,b,test))

