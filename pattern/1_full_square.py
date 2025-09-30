# 1.
# ****
# ****
# ****
# ****

for i in range(1,5):
    for j in range(1,6):
        print("*",end=" ")
    print()
    
    
#2.
 # *
 # * * 
 # * * *
#  * * * *

   
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*",end=" ")
    print()    
             
# 3.
#    *
#   **
#  ***
# ****
for i in range(1,5):
    for j in range(1,5):
        if j>=5-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        