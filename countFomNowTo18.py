import datetime

timenow = datetime.datetime.now().date()
When18 = datetime.datetime(2027, 10, 10).date()

print(f" I will be 18 in {(When18 - timenow)}")