# indexing
str="apna_college"
print(str[0])  # prints 'a'

print(str[4])  # print "_"(it will start from 0......)

print(str[8])  # prints 'l'

# Slicing :-> accessing parts of a string
# str[starting_index:ending_index]-.ending_index=(len(str)-1) 
# ending index is not included
sli="ApnaCollege"
print(sli[1:5]) #print 'pnaC'
print(sli[0:3]) #print 'Apn'
print(sli[:4]) # is same as sli[0:4] ->print 'Apna'
print(sli[5:]) # is same as sli[5:len(str)] ->print 'ollege'

# negative index
# Apple(-5,-4,-3,-2,-1)
ne_str="Apple"
print(ne_str[-1]) #print 'e'
print(ne_str[-3:-1]) #print 'pl'
print(ne_str[-5:-1]) #print 'Appl'