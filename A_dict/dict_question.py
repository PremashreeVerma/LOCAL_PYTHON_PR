#In this example, we will sort the dictionary by keys and the result type will be a dictionary. 

d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
mkey= list(d.keys())
mvalue= list(d.values())
mkey.sort()
print(mkey)
print(mvalue)
sd={}
for i in range(len(mkey)):
    sd[mkey[i]]=d[mkey[i]]
    print(mkey[i])
    print(d[mkey[i]])
print(sd)
print()

a = {'rohit': 10, 'suman': 9, 'sanjeev': 15}
akey= list(a.keys())
print(akey)
akey.sort()
newdict={}
for i in range(len(akey)):
    newdict[akey[i]]=a[akey[i]]
    
    print(newdict[akey[i]])
    print("hhhh: ",akey[i])
print(newdict)
# print(akey[i])
# print(a[akey[i]])
    # newdict
    # newdict[akey[i]]
    
#2 (sorted)

d = {2: 56, 1: 2, 5: 12, 4: 24}
print("dictionary:",d)
sd = dict(sorted(d.items()))
print(sd)
for i in sorted(d.keys()):
    print(i,end=" ")
print()

svkey=sorted(d.keys())
print(svkey)

# Creates a sorted dictionary (sorted by key)
# from collections import OrderedDict

d = {'ravi': '10', 'rajnish': '9', 'abc': '15'}
d1 = dict(sorted(d.items()))
print(d1)



n=["we","oiu","oi"]

for i in n:
    print(i)
    