def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """

    musbat=0
    if a>0:
       musbat +=1
    if b>0:
       musbat +=1
    if c>0:
       musbat +=1
    return musbat
print(main(-2,4,1))
print(main(3,-3,-6))