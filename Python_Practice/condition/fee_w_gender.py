gender=input("gender:")
cls=int(input("cls:")) #cls=class
if ((gender=="F"or"f" or"Female")and cls>=5):
    print("fee = 1000 for all subject" )
elif ((gender=="M" or "m"or"Male" )and cls>=5):
    print("fee = 1000 for all subject" )
elif ((gender=="M"or"m" or"Male") and cls<=5):
    print("fee = 500 for all subject" )
elif ((gender=="F"or"f" or"Female") and cls<=5):
    print("fee = 500 for all subject" )
else:
    print("invalid input")