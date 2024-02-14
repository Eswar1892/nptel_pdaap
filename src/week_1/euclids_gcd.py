
def euclid_gcd_recursive(m,n):

    if m<n:
        (m,n) = (n,m) # always ensures that m>n
    if m%n ==0:
        return n
    else:
        diff = m-n
        return euclid_gcd_recursive(max(n,diff), min(n, diff)) # Remember this return is a must to ensure result of the function that is called is passed back to the calling function


def euclid_gcd_while_loop(m,n):

    if m<n:
        (m,n) = (n,m)

    while m%n !=0:
        diff = m-n
        (m,n) = (max(n,diff),min(n,diff))

    return (n)