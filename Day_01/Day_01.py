with open('input.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

list1, list2 = [], []

for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

total = 0
for val1, val2 in zip(sorted(list1), sorted(list2)):
    total += abs(val1 - val2)

print(f'Part 1: total = {total}')


total = 0
for val1 in list1:
    total += list2.count(val1) * val1

print(f'Part 2: total = {total}')