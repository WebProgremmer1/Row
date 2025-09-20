import random

with open('hih.txt', 'r', encoding='utf-8') as file:
    students = [line.strip() for line in file]

#кто-то отстствует
l = input('Может кто-нибидь отсуствует?(да/нет):')
if l == 'да':
    k = int(input('Номер учащегося?'))
    del students[k]
else:
    pass

# рандом учеников
ran_nums = []
for j in range(len(students) // 2):
    ran_num = random.sample(students, 2)
    ran_nums.append(ran_num)
    for i in ran_num:
        students.remove(i)

l = int(input('Кол-во рядов? '))  # Запрашиваем количество рядов
ran_num = len(ran_nums) // l  # Количество студентов в одном ряду

# Добавляем метки для каждого ряда
grouped_students = [
    [f"Ряд {i + 1}: {i * (ran_num) + 1} - {(i + 1) * (ran_num)}"]
    for i in range(l)
]

for row in grouped_students:
    print(row)


# кол-во парт
def print_desks(ran_nums, single_student):
    for k, ran_num in enumerate(ran_nums, 1):
        print(f"Парта {k}: {ran_num}")
    if single_student:
        print(f'Один одинешенка: {single_student}')

# наказание ученику
single_student = students[0] if students else None
print_desks(ran_nums, single_student)
punish = input('Хотите наказать кого-то? (да/нет): ').lower()
if punish == 'да' and single_student:
    punish_stud = input('Имя холопа?').strip()
    punished = None
    for ran_num in ran_nums:
        if punish_stud in ran_num:
            punished = punish_stud
            ran_num.remove(punished)
            ran_num.append(single_student)
            single_student = punished
            break

    if punished:
        print("\nПосле наказания:")
        print_desks(ran_nums, single_student)
    else:
        print("Учащийся не найден.")
else:
    pass
