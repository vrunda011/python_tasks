# Creating Dictionaries

## empty_dict = dict()
empty_dict = {}
print(type(empty_dict))

student = {"name": "Krishna", "age": 32, "grade": 'A'}
print(student)

# Error

student = {"name": "Krishna", "age": 32, "name": 24}
print(student) # Output : {'name': 24, 'age': 32}

# Accessing Dictionary Elements

student = {"name": "Krishna", "age": 32, "grade": 'A'}
print(student['grade'])
print(student['age'])

# Accessing using get() method

print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name', "Not Available"))

# Modifying Dictionary Elements
## Dictionary are mutable, so you can add, update or delete elements

student["age"] = 33 ## updated value for the key
print(student)
student["address"] = "India" ## added a new key and value
print(student)

del student["grade"] ## delete key and value pair
print(student)

# Dictionary methods

keys = student.keys()
print(keys)
values = student.values()
print(values)

items = student.items()
print(items)

# shallow copy
student_copy = student
print(student)
print(student_copy)

student["name"] = "Krish1"
print(student)
print(student_copy)

student_copy1 = student.copy()
print(student_copy1)

student["name"] = "Krish2"
print(student)
print(student_copy1)

# Iterating over Dictionaries

## Iterating over keys
for key in student.keys():
    print(key)

## Iterating over values
for value in student.values():
    print(value)

## Iterating over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Nested Dictionaries
students = {
    "student1" : {"name":"krish", "age": 32},
    "student2" : {"name":"pritesh", "age": 30}
}
print(students)

# Access nested dictionaries elements
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info}")
    for key,value in student_info.items():
        print(f"{key}: {value}")

# Dictionary Comprehension
squares = {x:x**2 for x in range(5)}
print(squares)

# Conditional dictionary comprehension
evens = {x:x**2 for x in range(10) if x%2==0 }
print(evens)

# Merge 2 dictionaries into one

dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}
merged_dict = {**dict1, **dict2}
print(merged_dict)