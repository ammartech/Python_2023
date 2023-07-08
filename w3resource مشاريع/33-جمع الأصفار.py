#34
n1=int(input("الرقم الأول"))
n2=int(input("الرقم الثاني"))
n3=int(input("الرقم الثالث"))
sum=0
def sum_zero (n1,n2,n3):
    if n1==n2==n3:
        sum=0
    else:
        sum=n1+n2+3
    return sum

print(sum_zero(n1,n2,n3))
