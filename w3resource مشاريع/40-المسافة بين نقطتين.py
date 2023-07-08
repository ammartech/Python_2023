point_1 = input("أدخل النقطة الأولي").split()
point_2 = input("أدخل النقطة الثانية").split()

x1,y1=map(float,point_1)
x2,y2=map(float,point_2)

def calculate_distance(x1,y1,x2,y2):
    d=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
    return d
print(calculate_distance(x1,y1,x2,y2))
