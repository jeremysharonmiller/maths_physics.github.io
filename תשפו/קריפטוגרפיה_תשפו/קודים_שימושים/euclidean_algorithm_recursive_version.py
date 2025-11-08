# Input a and b
def EUCLID(a,b):
    if b==0:
        return a
    else:
        return EUCLID(b, a % b)

a = 289
b = 51

print(EUCLID(a,b))    