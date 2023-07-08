x = int(input("أدخل قيمة س"))
y = int(input("قيمة ص"))

def x_y_sq (x,y):
    final_sum = (x+y)**2
    print(f"({x}+{y})^2={final_sum}")
    return final_sum
x_y_sq(x,y)
