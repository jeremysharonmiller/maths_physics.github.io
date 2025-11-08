import math as m

# Input a and b
a = 289
b = 51

def EXTENDED_EUCLID(a,b):
    if b==0:
        return (a,1,0)
    (d1,s1,t1) = EXTENDED_EUCLID(b,a%b)
    (d ,s ,t ) =(d1,t1,s1-(a//b)*t1)
    return (d,s,t)

(d,s,t) = EXTENDED_EUCLID(a,b)

print( "\ns=%d, t=%d, d=%d"% (s,t,d))

test = d==m.gcd(a,b);

print( "\nTest: d = gcd(a,b):\n")

print( "%d == gcd(%d,%d), %s.\n"% (d,a,b,test))

test = s*a+t*b==d;

print( "\nTest: s*a+t*b = d:\n")

print( "%d*%d+%d*%d==%d , %s\n\n"% (s,a,t,b,d,test))


print(EXTENDED_EUCLID(a,b))    