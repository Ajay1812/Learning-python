import csv

students =[]

with open('students.csv') as file: 
    reader = csv.DictReader(file) #reader
    for row in reader:
        students.append({'name': row['name'], 'place': row['place']})

print(students)

# for student in sorted(students, key=lambda student:student['name']):
#     print(f"{student['name']} is from {student['place']}")