print("Practice List")

fruits=["apple", "banana", "mango", "orange", "grape"]

print(fruits)

print(fruits[2])
print(fruits[-1])
fruits.append("Kiwi")
print(fruits)

fruits.insert(1,"pineapple")
print(fruits)

fruits.remove("banana") #remove the value given
print(fruits)
fruits.pop()  # Removes last item
print(fruits)

# List Slicing
print(fruits[:3])

#  List Comprehension
# Task: Create a list of squares for numbers 1 to 10.
# [expression for item in iterable]
sq=[x**2 for x in range (1,11)]
print(sq)

Num=[1,2,3,4,5,6,7,8,9,10]
even_num=[n for n in Num if n%2==0]
print(even_num)

# Task: Sort the list in ascending and then descending order.

number=[12,32,11,2,435,6,89]
number.sort()
print("ascending",number)
number.sort(reverse=True)
print("descending",number)

# Task: Create a 3x3 matrix and print the second row.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])  # Second row

# Task: Write a function that takes a list of integers and returns a list with duplicates removed.
def remv_dup(lst):
    return(list(set(lst)))

dup_num=[1,3,5,4,5,4,2,9]
print(remv_dup(dup_num))

l=list(input("enter the list value"))
print(l)