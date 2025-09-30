# normal way to do factorial

# n=7

# fact=1
# for el in range(1,n+1):
#     fact=el*fact
# print(fact)

# with function now
# defining function
def factorial(n):
    n= int(n)
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    # return fact
    
# calling function
# factorial(5)   
fact_output= factorial(5) 
print("Output",fact_output)  # Output
    