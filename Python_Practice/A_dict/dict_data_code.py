import json

with open('dict_data','rt') as f:
    data=json.load(f)

print(type(data)) #<class 'list'>
print(data[1])
#{'id': 102, 'name': 'Bob', 'department': 'HR', 'skills': ['Recruitment', 'Payroll']}

print(data[1]['name'])  # Accessing a specific field in the dictionary

data[1]['skills'].append('AWS')
print(data[1])

# Adding a new skill to the skills list of the second dictionary in the list
data[1]['skills'].remove('Payroll')
print(data[1])  
# Removing a skill from the skills list of the second dictionary in the list

data.append({'id': 103, 'name': 'Prema', 'department': 'developer', 'skills': ['MDM', 'Excel','Python']})
# Adding a new dictionary to the list
print (data)
print(data[2]['name'])  # Accessing the name of the newly added dictionary

for d in data:
    if d['name'] == 'Prema':
       d['skills']= ['ETL', 'RELTIO']  # Replacing the skills list with a new one
        # # d['skills'].append('ETL', 'RELTIO') #twice append will not work
        # d['skills'].append('ETL')      # Add 'ETL'
        # d['skills'].append('RELTIO')   # Add 'RELTIO'
print(data[2])  # Displaying the updated dictionary for 'Prema'


with open('dict_data_output','wt') as file:
    json.dump(data, file, indent=4)
print("Data has been written to dict_data_output file.")