'''print("Result")
mark=int(input("enter ur marks: "))
if mark>=90:
    print("grade: A ")
elif (mark<90 and mark>=80):
    print("grade: B ")
elif (mark<80 and mark>=70):
    print("grade: C")
else:
    print("grade: D")'''
    
# other approach
mark=int(input("enter ur marks: "))
if mark>=90:
   grade="A" 
elif (mark<90 and mark>=80):
   grade="B" 
elif (mark<80 and mark>=70):
   grade="C" 
else:
   grade="D" 
print("grade: ",grade)