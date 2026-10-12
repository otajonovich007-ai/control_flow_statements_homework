def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    return
    musbat=0
    manfiy=0    
    if a>0:
       musbat +=1
    if b>0:
       musbat +=1
    if c>0:
       musbat +=1
    if a<0:
       manfiy +=1
    if b<0:
       manfiy +=1
    if c<0:
       manfiy +=1
    if musbat>manfiy:
        return "kop nusbat sonlar bor"
    if manfiy>musbat:
        return "kop manfiy sonlar bor"
        print(main(-2,4,1))
        print(main(3,-3,-6))
    