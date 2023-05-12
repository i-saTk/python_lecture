import datetime

# print(datetime.datetime.now())
now = datetime.datetime.now()
d = f"{now:%Y/%m/%d-%H:%M}"
print(d)