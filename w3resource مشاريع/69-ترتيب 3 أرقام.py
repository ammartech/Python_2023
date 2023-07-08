def sort_3_int (x,y,z):
    minmum = min(x,y,z)
    maximum = max(x,y,z)
    middle=(x+y+z)-minmum-maximum
    return maximum , middle, minmum

while True:
    n_1=int(input(""))
    n_2=int(input(""))
    n_3=int(input(""))
    print(sort_3_int (n_1,n_2,n_3))
    
