# --- Day 6: Tuning Trouble ---
"""
Task 1 - 
Find the first position where the four most recently received characters were all different.
How many characters need to be processed before the first start-of-packet marker is detected? 
(i.e. basically the last position of the first unique marker identified in the string)

Task 2 - 
Basically the same thing except find the unique marker using 14 distinct characters
"""

with open("day6.txt") as f:
    datastream = f.read()
    # iterating through the string to find the first 4 characters which are unique (done by using set())
    task1_result = [
        (datastream[ind : ind + 4], ind + 4)
        for ind, i in enumerate(datastream)
        if (ind + 4 <= len(datastream)) and (len(set(datastream[ind : ind + 4])) == 4)
    ][0]
    
    task2_result = [
        (datastream[ind : ind + 14], ind + 14)
        for ind, i in enumerate(datastream)
        if (ind + 14 <= len(datastream)) and (len(set(datastream[ind : ind + 14])) == 14)
    ][0]

    print(f"{task1_result=} and {task2_result=}")