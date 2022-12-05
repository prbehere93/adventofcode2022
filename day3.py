"""
Task 1 - 
Each rucksack has two large compartments. 
All items of a given type are meant to go into exactly one of the two compartments.
Every item type is identified by a single lowercase or uppercase letter.
The list of items for each rucksack is given as characters all on a single line. 
A given rucksack always has the same number of items in each of its two compartments, 
so the first half of the characters represent items in the first compartment, 
while the second half of the characters represent items in the second compartment.

Find the errors - basically find the item types which appear in both the compartments of the rucksack and the sum of priorities of those item types
- Lowercase item types a through z have priorities 1 through 26.
- Uppercase item types A through Z have priorities 27 through 52.

Task 2 -
One group - every three lines of the input.
Find the common item in every 3 lines of the input 
Find the sum of priorities (each letter has same value as the previous task)
"""
import string

all_letters = string.ascii_letters


def find_priority(rucksack_items):  # task 1
    """
    Finds the common item and assigns it a priority number
    Converting the initial input strings to sets and finding the intersection amongst them to get the common_item
    """
    common_items = []
    for i, j in rucksack_items:
        # unpacking the final set obtained (assuming that only one common item exists)
        common_items.append(*(set(i) & (set(j))))

    common_items = [all_letters.find(i) + 1 for i in common_items]
    return sum(common_items)


def find_badge_priority(elven_groups):  # task 2
    common_badges = []
    for i, j, k in elven_groups:
        common_badges.append(*(set(i) & set(j)) & (set(k)))

    common_badges = [all_letters.find(i) + 1 for i in common_badges]
    return sum(common_badges)


with open("day3.txt") as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

    # Divide the items of the rucksack by compartment (each compartment has the same no. of items)
    rucksack_items = [(i[: int(len(i) / 2)], i[int(len(i) / 2) :]) for i in lines]

    elven_groups = [
        (lines[i], lines[i + 1], lines[i + 2]) for i in range(0, len(lines) - 2, 3)
    ]

    task1_result = find_priority(rucksack_items)
    task2_result = find_badge_priority(elven_groups)
    print(f"Final result task 1 - {task1_result}")
    print(f"Final result task 2 - {task2_result}")
