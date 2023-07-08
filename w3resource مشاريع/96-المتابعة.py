import traceback

print('')
def f_1 (): return f_2()
def f_2 (): traceback.print_stack()
print(f_1())
