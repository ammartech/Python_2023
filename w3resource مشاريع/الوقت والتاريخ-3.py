from datetime import datetime
now = datetime.now()
time_to_format = now.strftime("%d %m %Y %H:%M:%S")
print("Current Time", time_to_format)
