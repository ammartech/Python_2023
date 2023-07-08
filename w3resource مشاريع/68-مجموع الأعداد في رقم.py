def sum_of_digits(num_entry):
    sum_of_numbers=0
    digit = num_entry %10
    sum_of_numbers+=digit
    num_entry =num_entry //10
    digit = num_entry %10
    sum_of_numbers+=digit
    num_entry=num_entry//10
    digit = num_entry %10
    sum_of_numbers+=digit
    num_entry=num_entry//10
    return sum_of_numbers

while True:
    num_entry = int(input("أدخل الرقم المراد إختباره"))
    print(sum_of_digits(num_entry))
