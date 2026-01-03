import datetime 

MyBirthDay = datetime.datetime(2009, 10, 10)
CurrentDay = datetime.datetime.now()

print(f"You Lived for : \n {(CurrentDay - MyBirthDay).days} Days \n {((CurrentDay - MyBirthDay)/365).days} Years")