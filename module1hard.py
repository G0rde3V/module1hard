grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_1 = sorted(students)

grades_1 = []
for num in grades:
    a = sum(num)/len(num)
    grades_1.append(a)

dict = dict(zip(student_1, grades_1))
print(dict)