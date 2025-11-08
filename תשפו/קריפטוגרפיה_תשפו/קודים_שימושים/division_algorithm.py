# Rotman p.38 

# Input a and b 
a= -66
b= -17

r=abs(a)
q=0

while r>= abs(b) :
    r=r-abs(b)
    q=q + 1

if a < 0:
    q=-q-1
    r=abs(b)-r

if b < 0:
    q = -q
    
print( "r=%d\nq=%d"% (r,q))

test = a==q*b+r;

print( "\nTest a = qb+r:\n")

print( "%d == %d * %d + %d, %s\n\n"% (a,q,b,r,test))

test = 0<= r< abs(b);

print( "\nTest 0 <= r <  |b|:\n")

print( "%d <= %d <  %d , %s\n\n"% (0,r,b,test))
