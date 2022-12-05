"""
Day 4 - Camp Cleanup
Task 1
Compare section assignments of elf pairs and find out the places where one of their assignments fully contains the other.
For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
How many such assignment pairs are present.
"""
import csv

elven_pairs = []
with open("day4.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        elven_pairs.append([row[0].split("-"), row[1].split("-")])

# count = 0
# print(len(elven_pairs))
# for i in elven_pairs:
#     if i[0] == i[1]:
#         count = count + 0
#     elif ((i[0][0] >= i[1][0]) and (i[0][1] <= i[1][1])) or (
#         (i[1][0] >= i[0][0]) and (i[1][1] <= i[0][1])
#     ):
#         # print(i)
#         count = count + 1
# print(f"Task 1 result - {count}")

# Alternative logic using the inbuilt range
count = 0
for i in elven_pairs:
    if (
        set(range(int(i[0][0]), int(i[0][1]) + 1)).issubset(
            set(range(int(i[1][0]), int(i[1][1]) + 1))
        )
    ) or (
        set(range(int(i[1][0]), int(i[1][1]) + 1)).issubset(
            set(range(int(i[0][0]), int(i[0][1]) + 1))
        )
    ):
        count = count + 1

print(f"Task 1 result - {count}")

# Note 580 is the correct answer (try to figure it out without using range)

"""
Task 2 - finding any overlap between the 2 assignment pairs
"""
count = 0
for i in elven_pairs:
    if set(range(int(i[0][0]), int(i[0][1]) + 1)).intersection(
        set(range(int(i[1][0]), int(i[1][1]) + 1))
    ):
        count = count + 1

print(f"Task 2 result - {count}")
