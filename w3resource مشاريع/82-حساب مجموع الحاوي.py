Tuple =(2,6,6,43,22,21)
def Tuple_sum (Tuple):
    print(type(Tuple))
    print(Tuple)
    return sum(Tuple)
print(Tuple_sum(Tuple))
print("--"*20)
List=[3,6.5,54,42,112,12,12.6]
def List_sum (List):
    print(type(List))
    print(List)
    return sum(List)
print(List_sum(List))
print("--"*20)
dic ={'Ali':101,'Ahmed' :102 , 'Ammar':103}
def dict_sum(dic):
    print(type(dic))
    print(dic)
    print()
    total_sum=0
    for i in dic:
        total_sum +=dic[i]
    return total_sum
print(dict_sum(dic))
print("--"*20)
set_1={34,66,43,23,78,12}
def Set_sum (set_l):
    print(type(set_l))
    print(set_l)
    return sum(set_l)
print(Set_sum(set_1))


