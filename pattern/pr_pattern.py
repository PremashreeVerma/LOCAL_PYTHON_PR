# # 1.
# # *
# # **
# # ***
# # ****
# # *****

# for i in range(0,5):
#     for j in range(0,5):
#         if i>= j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range (5):
#     for j in range (i+1):
#         print("*",end=" ")
#     print()
    
# # 2.
# # *****
# # ****
# # ***
# # **
# # *
# # OR
# # (it is working as per the condition but because the is no else condition at last what is coming we can see the result in srink  form)
# # 0 1 2 3 4
# # 1 2 3 4
# # 2 3 4
# # 3 4
# # 4

# for i in range (0,5):
#     for j in range(0,5):
#         if j>=i:
#             print(j,end=" ")
        
#     print()

# # 3.
# # 0 1 2 3 4
# #   1 2 3 4
# #     2 3 4
# #       3 4
# #         4
# for i in range (0,5):
#     for j in range(0,5):
#         if j>=i:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# # .4
# # 4
# # 3 4
# # 2 3 4
# # 1 2 3 4


# for i in range (1,5):
#     for j in range(1,5):
#         if j>=5-i:
#             print(j,end=" ")
       
#     print()
   
   
# # 5. 
# #       4
# #     3 4
# #   2 3 4
# # 1 2 3 4  
    
# for i in range (1,5):
#     for j in range(1,5):
#         if i>=5-j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")   
#     print()
# print()

    
    
    
# for i in range (1,8):
#     for j in range(1,5):
#         if i<=5-j or i<=8-j :
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")   

#     print()

# for i in range(1, 10):
#     for j in range(1, 5):
#         if i < 5:
#             if i >= 5 - j :
#                 print(j, end="")
#             else:
#                 print(" ", end="")
#         else:                           
#             if j <= i - 4:
#                 print(" ", end="")
#             else:
#                 print(j, end="")
#     print()

#  # square


for i in range (5):
    for j in range (5):
        if i==0 or i==5-1 or j==0 or j==5-1:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

for i in range (5):
    for j in range (5):
        if i==j or 4==j+i:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

for i in range (5):
    for j in range (5):
        if i==j or j==0 or i==5-1:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

for i in range (5):
    for j in range (5):
        if i==j or j==0 or i==5-1 or j==5-1 or i==0 or j+i==4:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

for i in range (5):
    for j in range (5):
        if i==2 or j==0 or j==5-1:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

for i in range (5):
    for j in range (5):
        if i==2 or j==0 or j==5-1:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
print()


# A-Z:

# A
for i in range (5):
    for j in range (5):
        if i==2 or j==0 or j==5-1 or i==0:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
print()    


# B
for i in range (5):
    for j in range (5):
        if i==2 or j==0 or j==5-1 or i==0 or i==5-1:
           print("*",end=" ") 
        elif j==5-1 :
               print("*",end=" ") 
           
        else:
            print(" ",end=" ")
    print()
print()

# B
for i in range (5):
    for j in range (5):
        if j==0 :
            print("*",end=" ")
        elif (i==0 or i==2 or i==5-1)and j!=4 :
            print("*",end=" ") 
        elif j==5-1 and (i==1 or i==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
 

# C
for i in range (5):
    for j in range (5):
        if j==0 or i==5-1 or i==0:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
print()

## C
for i in range (5):
    for j in range (5):
        if (i==5-1 and (j!=0 ))  :
           print("*",end=" ") 
        elif (i==0)  and i!=j:   
            print("*",end=" ") 
        elif (j==0)  and (i<4  and i>0):   
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
print()

# D
for i in range (5):
    for j in range (5):
        if i==5-1 or j==0 or j==5-1 or i==0:
           print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
print()

# # D
for i in range (5):
    for j in range (5):
        if (j==0 or i==0 or i==5-1)and j!=4:
           print("*",end=" ") 
        elif (j==5-1)and (i<4 and i>0):
               print("*",end=" ") 
        else:
            print(" ",end=" ")
    print() 
print()

# E

for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==5-1 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# F

for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# G

for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==5-1 :
            print("*",end=" ")
        elif j==5-1 and i!=1:
            print("*",end=" ")
        elif i==2 and j!=1:
            print("*",end=" ")
            
        else:
            print(" ",end=" ")
    
            
    print()
print()


# H
for i in range(5):
    for j in range(5):
        if j==5-1 or j==0 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# I
for i in range(5):
    for j in range(5):
        if i==5-1 or i==0 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# J
for i in range(5):
    for j in range(5):
        if i==0 or j==2:
            print("*",end=" ")
        elif i==5-1 and j<3:
            print("*",end=" ")
        elif j==0 and i>2:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
            
    print()
print()

# K
for i in range(5):
    for j in range(5):
        if j==0 or j==3-i or j== i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# L
for i in range(5):
    for j in range(5):
        if i==5-1 or j==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# M
for i in range(5):
    for j in range(5):
        if j==5-1 or j==0 :
            print("*",end=" ")
        elif i==j and j<3 :
            print("*",end=" ")
        elif i+ j==4 and j>2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# N
for i in range(5):
    for j in range(5):
        if j==0 or j==5-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# O
for i in range(5):
    for j in range(5):
        if j==5-1 or j==0 or i==0 or i==5-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()


# P
for i in range(5):
    for j in range(5):
        if j==0 or i==0 or i==2 :
            print("*",end=" ")
        elif j==5-1 and i<3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# Q
for i in range(5):
    for j in range(5):
        if j==0 and i!=5-1 :
            print("*",end=" ")
        elif i==4-1 and j!=5-1:
            print("*",end=" ")
        elif i==0 and j!=5-1:
            print("*",end=" ")
        elif j==5-1  :
            print("*",end=" ")
        elif j==i and j!=1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()


# R
for i in range(5):
    for j in range(5):
        if j==0 or i==0 or i==2  or j== i-1:
            print("*",end=" ")
        elif j==5-1 and i<3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# S
for i in range(5):
    for j in range(5):
        if i==0 or i==5-1 or i==2:
            print("*",end=" ")
        elif j==0 and i<2:
            print("*",end=" ")
        elif j==5-1 and i>2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# T
for i in range(5):
    for j in range(5):
        if i==0 or j==3-1 :
            print("*",end=" ")
        # elif j==0 and i<2:
        #     print("*",end=" ")
        # elif j==5-1 and i>2:
        #     print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# U
for i in range(5):
    for j in range(5):
        if i==5-1 or j==0 or j==5-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# V
for i in range(5):
    for j in range(10):
        if i==j or i+j== 8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# W
for i in range(5):
    for j in range(10):
        if i==j or i+j== 8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# W
for i in range(5):
    for j in range(5):
        if j==5-1 or j==0 :
            print("*",end=" ")
        elif i==j and j>=2 :
            print("*",end=" ")
        elif i+ j==4 and j<2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# X
for i in range(5):
    for j in range(5):
        if i==j or i+ j==4  :
            print("*",end=" ")
        
        else:
            print(" ",end=" ")
            
    print()
print()

# Y
for i in range(5):
    for j in range(5):
        if j==3-1 and i>=2 :
            print("*",end=" ")
        elif i==j and j<3 :
            print("*",end=" ")
        elif i+ j==4 and j>2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
print()

# Z
for i in range(5):
    for j in range(5):
        if i==0 or i==5-1 or i+j==4:
            print("*",end=" ")

        else:
            print(" ",end=" ")
            
    print()
print()



