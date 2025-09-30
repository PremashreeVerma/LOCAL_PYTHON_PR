# Task: Create a tuple of 5 city names and print it.
cities=("New York", "Paris", "Tokyo", "Sydney", "Mumbai")
print(cities)

# Task: Print the first and last city.
print(cities[2])
print(cities[-2])
print(cities[-1])

# Task: Unpack a tuple of 3 values into separate variables.
person=("Simran",26,"Jamshedpur")
Name,age,City=person
print(person)
print(Name)

# Task: Loop through the `cities` tuple and print each city.
for citi in cities: #for variable in list/tuple
    print(citi)

# Task: Check if "Tokyo" is in the tuple.
if "Tokyo" in cities:
    print("Yes Present")
    
# Task: Use `count()` and `index()` methods on a tuple.
num=(1,2,2,4,3,5,6,5,6,2,5,2,2)
print(num.count(5))  # Count occurrences of 2
print(num.index(3))  # Index of first occurrence of 3

# Task: Print the first three elements from the tuple.

print(num[:5])
print(num[3:9])
print(num[6:])

# Task: Access element inside a nested tuple.
nested=((2,3,1),(2,4,6),(6,7,8))
print(nested[2][1])

# Task: Convert a list to a tuple and back.

fruits=["apple","orange","banana"]
f_t= tuple(fruits)
print(f_t)

lang=("Hindi","english","Spanish")
lang_list=list(lang)
print(lang_list)

# Task: Write a function that takes a tuple of numbers and returns a new tuple with only the even numbers.
def fun_num(tup):
    even_num =[x for x in tup if x % 2 ==0 ]
    return tuple(even_num)
print(fun_num((2,4,5,6,7,8,97,4,12,16)))

# Concatenation (+)
a = (1, 2, 3)
b = (4, 5)
c = a + b
print(c)
#  Repetition (*)
a = ("Hi",) * 3
print(a) # Output: ('Hi', 'Hi', 'Hi')

# Membership Test (in)
colors = ("red", "blue", "green")
print("red" in colors) #Output=True
print("Yellow" in colors) #Output=False

# Length
t = (10, 20, 30, 40)
print(len(t)) # Output: 4

# Maximum and Minimum
nums = (10, 50, 30, 5)
print(max(nums))  # Output: 50
print(min(nums))  # Output: 5