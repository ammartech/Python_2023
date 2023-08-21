def variable_or_otherwise(var):

    return var in locals() or var in globals()

t=554
r=76
e=66

print(variable_or_otherwise("v"))
print(variable_or_otherwise("e"))
print(variable_or_otherwise("o"))
