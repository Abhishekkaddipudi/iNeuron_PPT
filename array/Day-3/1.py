def pow(x,n):
    if n==0:
        return 1
    if n<0:
        n=-n
        x=1/x
    return pow(x*x,n/2) if (n%2==0) else x*pow(x*x,n/2) 

print(pow(2,3))