from collections import defaultdict

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

groups = dict()

for student, group in students:
    if group not in groups:
        groups[group] = list()
    groups[group].append(student)
    
print(groups)
print()

groups_1 = defaultdict(list)

for student, group in students:
    groups_1[group].append(student)

print(groups_1)
print()
print(groups_1[2021])
print()
print(groups_1)


