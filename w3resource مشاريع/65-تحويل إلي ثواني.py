def convert_seconds (seconds):
    days= seconds//(24*3600)
    seconds %= (24*3600)
    hours= seconds //3600
    seconds %=3600
    minutes =seconds // 60
    seconds %= 60
    return days, hours , minutes, seconds

while True:
    total_seconds= int(input(""))
    print(convert_seconds (total_seconds))
