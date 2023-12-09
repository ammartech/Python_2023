def Separate_words():
    n=int(input(" أدخل الرقم المطلوب اقتطاع الرقم منه"))
    word=str(input("أدخل الكلمة المطلوبة"))
    Output_word=word[::n]
    print(Output_word)

while True :
    print('''برنامج إقتطاع الكلمات \n 1.لدخول البرنامج  \n 2.للخروج''')

Separate_words()

