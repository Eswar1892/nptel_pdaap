
def improved_gcd(m,n):

    for i in range (min(m,n)+1,0,-1):
        if m%i == 0 and n%i ==0:
            return i



print(improved_gcd(14,4))