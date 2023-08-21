import  os

print([f for f in os.listdir('D:/')if os.path.isfile(os.path.join('D:/',f))])
