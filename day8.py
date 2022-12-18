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

for ind, tree in enumerate(trees):
    # ind above is the row
    # the index below is the column
    for index, j in enumerate(tree):
        # ignoring the first and last entry in row
        # In case of the first row and the last row or the first or last index of the list perform this
        if ind == 0 or ind == len(trees) - 1 or index == 0 or index == len(tree) - 1:
            visible_trees = visible_trees + 1
            continue
        current_tree = j
        max_left_trees = max(tree[:index])
        max_right_trees = max(tree[index + 1 :])
        max_top_tree = max(transposed_trees[index][:ind])
        max_bottom_tree = max(transposed_trees[index][ind + 1 :])
        if (
            (j > max_bottom_tree)
            or (j > max_left_trees)
            or (j > max_right_trees)
            or (j > max_top_tree)
        ):
            visible_trees = visible_trees + 1

print(f"Task 1 = {visible_trees}")

executionTime = time.time() - start_time
print(executionTime)
