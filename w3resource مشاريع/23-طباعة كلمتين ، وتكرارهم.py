def copies_char(string,n):
    if len(string)<2:
        result= string*n
    else:
        result =string[:2]*n
    return result

word_is= str(input("أدخل النص"))
num_copies=int(input("أدخل عدد مرات التكرار"))

new_output= copies_char(word_is,num_copies)
print(new_output)
