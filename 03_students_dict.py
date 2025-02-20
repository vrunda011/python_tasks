students = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}
total_marks = {}
subject_counts = {}

# Total marks of each student
for key, value in students.items():
    name = key.split('-')[0]
    if name in total_marks:
        total_marks[name] += value
        subject_counts[name] += 1
    else:
        total_marks[name] = value
        subject_counts[name] = 1

print(total_marks)

# Average marks of each student
average_marks = {}
for name in total_marks:
    average_marks[name] = total_marks[name] / subject_counts[name]

print(average_marks)


# Student with max marks
max_mark = max(total_marks, key=total_marks.get)
print(f"Top student: {max_mark}, Marks: {total_marks[max_mark]}")

# Subject-wise max marks
subjects = {}
for key, value in students.items():
    sub = key.split('-')[1]
    if sub in subjects:
        subjects[sub] = max(subjects[sub], value)
    else:
        subjects[sub] = value

print(subjects)

# Sort Students by Total Marks in Descending Order
sorted_dict = dict(sorted(total_marks.items(), reverse=True))

print(sorted_dict)