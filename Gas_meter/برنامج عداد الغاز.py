import getpass
username = getpass.getuser()
print("مرحبا بك:", username)
import matplotlib.pyplot as plt

ID= input("رقم العداد التسلسلي")

# Function to read the gas meter and calculate the consumption
def Count(counts_list, n_old=0):
    t = int(input("أدخل عدد القراءات: "))
    for i in range(t):
        subscribe = str(input("هل أنت مشترك جديد أم سابق (ج/س)"))
        
        if subscribe == 'ج':
            n_current = int(input("أدخل قيمة العداد: "))
            count = n_current
        elif subscribe == 'س':
            n_current = int(input("أدخل قيمة العداد: "))
            n_old = int(input("أدخل القراءة السابقة: "))
            count = n_current - n_old
        else:
            print("خطأ في إدخال البيانات.")
            continue
        
        if count < 0:
            print("خطأ، أدخل القيمة مرة أخرى.")
            n_current = int(input("أدخل القراءة الحالية: "))
            count = n_current
        
        counts_list.append(count)
        n_old = n_current
        
        print("الإستهلاك الحالي:", count)
    
    return counts_list


def show_counts(counts_list):
    print("قيم الإستهلاك هي:")
    for i in range(len(counts_list)):
        print(f"{i+1}. {counts_list[i]}")
    delete = str(input("هل تريد حذف قيمة من البيانات الموجودة (نعم/لا)"))
    if delete == "نعم":
        delete_confirm = int(input("ما القيمة التي تريد حذفها"))
        if delete_confirm in counts_list:
            counts_list.remove(delete_confirm)
            print("تمت الحذف")
            print(counts_list)
        else:
            print("القيمة المطلوبة غير موجودة في القائمة.")
    return counts_list



        
def plot_counts(counts_list):
    # Set up the x-axis values as a list of integers from 1 to the length of the counts_list
    x_values = list(range(1, len(counts_list)+1))
    # Create a new figure and axis for the plot
    fig, ax = plt.subplots()
    # Plot the counts_list as a line graph with the x-axis values as the index
    ax.plot(x_values, counts_list)
    # Set the x-axis and y-axis labels
    ax.set_xlabel('القراءات (ن)')
    ax.set_ylabel('الإستهلاك')
    #The title
    plt.title("رسم بياني")
    # Show the plot
    plt.show()

# Main program
counts_list = []
count_loop =0
while True:
    print("--"*30)
    print(f''' ___________________
|  _________________  |
| |                 | |
| | برنامج الغاز    | |
| |    _______      | |
| |  /         \    | |
| | |  غاز 10m³ |   | |
| |  \_________/    | |
| |                 | |
| |  رقم تسلسلي     | |
| |  {ID}   | |
| |_________________| |
|_____________________| 
 ''')
    print("مرحبا بكم في برنامج الغاز")
    print("1. قراءة قياس الغاز.")
    print("2. عرض الإستهلاك.")
    print("3. الخروج.")
    print("4. عمل رسم إحصائي")
    choice = int(input("الإحتيار هو: "))
    if choice == 1:
        counts_list = Count(counts_list)
    elif choice == 2:
        show_counts(counts_list)
    elif choice == 3:
        print("الوداع!")
        break
    elif choice ==4:
        plot_counts(counts_list)
    else:
        print("خطأ , أدخل القيمة  الصحيحة.")
