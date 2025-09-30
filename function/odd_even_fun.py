# function for checking odd n even
def check_odd_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
num=int(input("enter a number to check its odd or even: "))
print(check_odd_even(num))
