"""
Task 1 - 
1st col : A - Rock, B - Paper, C - Scissors
2nd col : X - Rock, Y - Paper, Z - Scissors

Score Calculation - 
The score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus 
the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

import csv

# conditions for win, loss, draw -
conditions = {
    "win": ["AY", "BZ", "CX"],
    "loss": ["AZ", "BX", "CY"],
    "draw": ["AX", "BY", "CZ"],
}

# points = {"win": 6, "loss": 0, "draw": 3, "X": 1, "Y": 2, "Z": 3}

strategy_guide = []
with open("day2.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        strategy_guide.append(row[0].replace(" ", ""))

print(strategy_guide)

result_points = [
    6 if i in conditions["win"] else (0 if i in conditions["loss"] else 3)
    for i in strategy_guide
]

other_points = [1 if "X" in i else (2 if "Y" in i else 3) for i in strategy_guide]

print(
    f"Final points from strategy guide (task 1) {sum(result_points)+sum(other_points)}"
)

"""
Task 2 -
The second column says how the round needs to end: 
-X means you need to lose
-Y means you need to end the round in a draw
-Z means you need to win
"""
# A dictionary to keep track of the points that you are supposed to get for every outcome
# eg if the opponent chooses rock and if you want to win you will choose paper so the no. of points will be
# points from paper (2) + points from winning (3)
conditions = {
    "A": {"win": 6 + 2, "draw": 3 + 1, "loss": 0 + 3},
    "B": {"win": 6 + 3, "draw": 3 + 2, "loss": 0 + 1},
    "C": {"win": 6 + 1, "draw": 3 + 3, "loss": 0 + 2},
}

final_points = [
    conditions[i[0]]["loss"]
    if "X" in i
    else (conditions[i[0]]["draw"] if "Y" in i else conditions[i[0]]["win"])
    for i in strategy_guide
]

print(f"Final points from strategy guide (task 2) {sum(final_points)}")
