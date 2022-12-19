# --- Day 8: Treetop Tree House ---
"""
Task 1- 
Input is the height of each tree (from 0 to 9)
A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
Only consider trees in the same row or column;
All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view.
Note - count the trees on the outside grid as visible

Task 2 -
Find the highest scenic score possible.
To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
(If a tree is right on the edge, at least one of its viewing distances will be zero.)
"""
import time
import csv
import itertools

start_time = time.time()
trees = []
with open("day8.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        trees.append(list(row[0]))

transposed_trees = list(map(list, zip(*trees)))  # transpose of the tree list
visible_trees = 0
all_scores = []
for ind, tree in enumerate(trees):
    # ind above is the row
    # the index below is the column
    for index, j in enumerate(tree):

        current_tree = j
        left_trees = tree[:index]
        right_trees = tree[index + 1 :]
        top_trees = transposed_trees[index][:ind]
        bottom_trees = transposed_trees[index][ind + 1 :]

        # check if there are any other trees around the current tree
        if left_trees or right_trees or top_trees or bottom_trees:
            left_score = [
                left_ind for left_ind, i in enumerate(left_trees[::-1]) if i >= j
            ]
            right_score = [
                right_ind for right_ind, i in enumerate(right_trees) if i >= j
            ]
            top_score = [top_ind for top_ind, i in enumerate(top_trees[::-1]) if i >= j]
            bottom_score = [
                bottom_ind for bottom_ind, i in enumerate(bottom_trees) if i >= j
            ]

            # the below logic is slightly confusing, essentially get the first element of the list if the list exists
            # else if the tree is on the edge it will be 0, othewise there is no other tree i.e. >= the height of the current tree
            left_score = index if not left_score else left_score[0] + 1
            right_score = (
                (len(tree) - 1) - index if not right_score else right_score[0] + 1
            )
            top_score = ind if not top_score else top_score[0] + 1
            bottom_score = (
                (len(trees) - 1) - ind if not bottom_score else bottom_score[0] + 1
            )

            all_scores.append(left_score * right_score * top_score * bottom_score)
            print(
                f"""Row Col - {ind},{index}, current tree - {j}, left score - {left_score}, right score - {right_score}, top score - {top_score}, bottom score - {bottom_score}"""
            )

        # ignoring the first and last entry in row
        # In case of the first row and the last row or the first or last index of the list perform this
        if ind == 0 or ind == len(trees) - 1 or index == 0 or index == len(tree) - 1:
            visible_trees = visible_trees + 1
            continue

        max_left_trees = max(left_trees)
        max_right_trees = max(right_trees)
        max_top_tree = max(top_trees)
        max_bottom_tree = max(bottom_trees)
        if (
            (j > max_bottom_tree)
            or (j > max_left_trees)
            or (j > max_right_trees)
            or (j > max_top_tree)
        ):
            visible_trees = visible_trees + 1

print(f"Task 1 = {visible_trees}")
print(f"Task 2 = {max(all_scores)}")

executionTime = time.time() - start_time
print(executionTime)
