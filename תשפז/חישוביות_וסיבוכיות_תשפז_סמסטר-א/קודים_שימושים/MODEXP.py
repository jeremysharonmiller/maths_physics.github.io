# Input a,b,c,p

def get_binary_digits(x):
    bin_digits_str   = bin(x)[2:]
    bin_digits_chars =  list(bin_digits_str)
    bin_digits       = [int(a) for a in bin_digits_chars]
    return bin_digits
    
a = 3 
b = 4 
c = 84 
p = 3
x = a % p

b_bin = get_binary_digits(b)
n     = len(b_bin)

i = 0
y = 1

while i<= n:
    bi = b_bin[n-i-1]
    if bi == 1:
        y = y*(x % p)
    x = (x**2 % p)
    i = i + 1

if y == c % p:
    print('accept')
else:
    print('reject')