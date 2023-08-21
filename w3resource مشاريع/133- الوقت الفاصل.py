import time

now_1=time.time()

def Ali (Name,Age,R):
    print(Name,Age,R)
    return Name,Age,R

Ali('Ammar','24','R+')
now_2=time.time()

d_time=now_2-now_1

print("%.5f"%(d_time*0.016) ,'دقائق')
