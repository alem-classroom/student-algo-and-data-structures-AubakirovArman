def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    fac=0
    fac2=1
    for i in range(7):
        d=fac+fac2
        fac=fac2
        fac2=d
    return fac
