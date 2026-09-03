import math as m

# Input a and b 
a = 26
b = 19

r = [0]*100; s = [0]*100; t = [0]*100; q = [0]*100;

n = 1

r[0] = abs(a)  #r0
r[1] = abs(b)  #r1

s[0] = 1  #s0
s[1] = 0  #s1

t[0] = 0  #s0
t[1] = 1  #s1

while r[n] !=  0:
    q[n]     = r[n-1] // r[n] 
    r[n + 1] = r[n-1] - q[n]*r[n]
    s[n + 1] = s[n-1] - q[n]*s[n]
    t[n + 1] = t[n-1] - q[n]*t[n]
    print("n=%d, q=%d, r=%d, s=%d, t=%d \n" % (n,q[n],r[n+1],s[n+1],t[n+1]))
    
    test = r[n] == s[n]*a + t[n]*b
    print(test)
    
    n        = n+1

n = n-1
d = r[n]
s = s[n]
t = t[n]
    
print( "\ns=%d, t=%d, d=%d"% (s,t,d))

test = d==m.gcd(a,b);

print( "\nTest: d = gcd(a,b):\n")

print( "%d == gcd(%d,%d), %s.\n"% (d,a,b,test))

test = s*a+t*b==d;

print( "\nTest: s*a+t*b = d:\n")

print( "%d*%d+%d*%d==%d , %s\n\n"% (s,a,t,b,d,test))
