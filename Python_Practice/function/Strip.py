def remove(l,word):
    for item in l:
        l.remove(word)
        return l
l=["Harry","Rohit","Srinu","an"]
word=str(input("enter a word to remove : "))
print(remove(l,word))

def strip(lst,word):
    n=[]
    for item in lst:
        if not(item==word):
            n.append(item.strip(word))
    return n
lst=["Harry","Rohan","Srinu","an"]
word=str(input("enter a word to remove : "))
print(strip(lst,word))
