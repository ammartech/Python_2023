import time

start_time = time.time()

def hi_print():
    print("أحمس")
    y=3
    area=y**3
    return area
hi_print()

final_time=time.time()

exe_time=final_time -start_time

print("الوقت:" , exe_time)
