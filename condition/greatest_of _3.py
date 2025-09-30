# WAP tp find the greatest of three no.
num1=int(input("Enter the first no."))
num2=int(input("Enter the second no."))
num3=int(input("Enter the thrid no."))

if num1>num2 and num1>3:
    print("The greatest no. is",num1)
elif num2>num1 and num2>num3:
    print("The greatest no. is",num2)
else:
    print("The greatest no. is",num3)