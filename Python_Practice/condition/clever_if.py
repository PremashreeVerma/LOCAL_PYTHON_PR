age=int(input("age: "))
# syntax:
# <var>=(false_val,true_val)[condition]
vote=("yes","no")[age<=18]
print(vote)

# salarya and tax count
sal=float(input("salary="))
tax=sal*(0.1,0.2)[sal>=50000]
print(tax)