# import os
data={'one':1, 'two':2, 'three':3}
print(data['one'])

# #if any key is not present, it will raise a KeyError
#print(data['four'])  # Uncommenting this line will raise a KeyError

# to avoid KeyError, use the get method
print(data.get('four')) # This will return "None" if 'four' is not found, instead of raising an error
## to avoid KeyError, you can also provide a default value
print(data.get('four', 'Not Found'))  # This will return "Not Found"


keys=['one', 'two', 'three', 'four']
values=['java', 'python', 'c++', 'javascript']
new_dict= dict(zip(keys,values))
# This will create a dictionary by pairing keys and values


new_dict['five']= 'ruby'
# This will add a new key-value pair to the dictionary 
print(new_dict)

del new_dict['four']
# This will delete the key 'four' from the dictionary
print(new_dict)


prog={'JS':'Atom', 'Python':['PyCharm','sublime'], 'Java':{'JEE':'Eclipse','JSE': 'NetBeans'},'css':['VS Code', 'Sublime']}
# This is a nested dictionary with different data types
print(prog['JS'])  # Accessing a value using a key

print(prog['Python'])  # Accessing a list value
print(prog['Python'][1])  # Accessing an element from the list
print(prog['Java']['JEE'])  # Accessing a value from a nested dictionary






# # Ensure the directory exists
# os.makedirs('A_dict', exist_ok=True)

## Create a new file (or overwrite if it exists)
#with open('newfile.txt', 'wt') as fl:
#    fl.write('This is a new file created using Python.')

#print("File created successfully.")

#with open('newfile.txt', 'rt') as fl:
#    con = fl.read()
#    print("Content of the file:", con)


