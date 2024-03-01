# with open("students.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(',')
#         print(f"{name} from {place}")



# with open('students.csv', 'r') as file:
#     for line in sorted(file):
#         name, place = line.rstrip().split(',')
#         print(f"{name} from {place}")

students = []

with open('students.csv') as file:
    for line in file:
        name, place = line.rstrip().split(',')
        # student = {}
        # student['name'] = name
        # student['place'] = place
        # students.append(student)
        student = {'name': name, 'place': place}
        students.append(student)
# def get_name(student):
#     return student['name']

# def get_place(student):
#     return student['place']

for student in sorted(students,key=lambda student: student['name']): # key = get_place, get_name
    print(f"{student['name']} from {student['place']} ")
