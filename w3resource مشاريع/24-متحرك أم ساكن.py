while True:
    letter = str(input("أدخل الحرف المراد إختباره"))

    vowels= ['a','e','i','o','u']
    letter_1 = letter.lower()
    if letter_1 in vowels:
        print("حرف متحرك")
    else:
        print("ليست كذلك")
