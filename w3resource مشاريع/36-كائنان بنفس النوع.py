def add_numbers(n1, n2):
    if not (isinstance(n1, int) and isinstance(n2, int)):
        return "لابد وأن يكونا رقمين"
    return n1 + n2

print(add_numbers(20, '43'))
print(add_numbers('rr', 40))
print(add_numbers(3,55))
