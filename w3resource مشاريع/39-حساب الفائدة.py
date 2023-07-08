amount =float(input("القيمة لرأس المال"))
interest_rate =float(input("نسبة الفائدة"))
years =float(input("عدد السنوات"))
def compound_interest(amount , interest_rate,years):
    interest= amount* (interest_rate/100)
    future_amount= interest*years +amount
    return future_amount

print(compound_interest(amount , interest_rate,years))
