# defination:-
# Range function returns a sequence of number, starting from 0 (by default)and increments by 1(by default), and stop before a specified no.
# syntax:- 
# range(start,stop,step)

seq=range(5)
print(seq[2])
print(seq[0])

seq=range(5)
for i in seq:
    print(i)
# output:-
# 0
# 1
# 2
# 3
# 4  


for i in range(5):# range(stop)
    print(i)    
# output:-
# 0
# 1
# 2
# 3
# 4

for i in range(2,5):# range(start,stop)
    print(i)   
# output:-
# 2
# 3
# 4

for i in range(2,10,2):# range(start,stop,step)
    print(i)   
# output:-
# 2
# 4
# 6
# 8