import matplotlib.pyplot as plt

#رسم الدوال الهستوجرام

def gen_histogram(info):
    plt.hist(info, bins='auto', color='red',alpha=0.3)
    plt.xlabel('القيم')
    plt.ylabel('التكرار')
    plt.title('الهستوجرام')
    plt.grid('True')
    plt.show()

data_test=[8,0,7,4,4,4,2,2,1,1,1,1,45,3,2,2,34,4,2]

gen_histogram(data_test)
