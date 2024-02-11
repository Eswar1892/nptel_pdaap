

def factors(m):

    x = []
    for i in range(1,m+1):
        if m%i==0:
            x.append(i)

    return x

def gcd(m,n):

    m_factors = factors(m)
    n_factors = factors(n)
    common_factors = []
    if len(m_factors) >= len(n_factors):  # TODO: is the if statement neccessary here? Does improve any efficieny?
        for i in n_factors:
            if i in m_factors:
                common_factors.append(i)
    else:
        for j in m_factors:
            if j in n_factors:
                common_factors.append(j)

    return common_factors[-1]



if __name__ == '__main__':

    print(gcd(14,12))
