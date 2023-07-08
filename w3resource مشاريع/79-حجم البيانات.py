import sys

def get_the_size(data):
    return sys.getsizeof(data)

test_ls =[6,8,9,44,98]

print(get_the_size(test_ls), "كمية البيانات")
