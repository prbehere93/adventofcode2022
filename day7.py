# --- Day 7: No Space Left On Device ---
"""
Input - commands to browse the directory (check the input)

Task 1 - 
The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly.
Find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.

Task 2 - 
The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. 
You need to find a directory you can delete that will free up enough space to run the update.

"""
import re
from pathlib import Path


def is_file(item):
    return bool(re.search(r"\d", item))


def is_dir(item):
    return bool(re.search(r"dir", item))


with open("day7.txt") as f:
    command_inputs = f.read().replace("$ ls", "")
    command_inputs = command_inputs.split("\n")
    # regex for identifying dirs and 'cd ..'
    dir_match_pattern = "[\$ cd \S+]"

result = []
parent_dir = Path()  # using this to store parent dir

# split the list into multiple sublists, each of which represent a single directory (or cd ..)
command_inputs_split = [
    i.split(",") for i in ",".join(command_inputs).split("$ ") if i != ""
]
command_inputs_split = [j for j in [i for i in command_inputs_split] if j != ""]

# creating a list of dicts, each of which stores the following -
# The current_directory, files in the current dir, directories in the current directory and the parent dir
for i in command_inputs_split:
    dir_struct = {"current_dir": [], "files": [], "dirs": [], "parent_dir": []}
    if i[0] == "cd /":
        dir_struct["parent_dir"] = Path("/")
    if i[0] == "cd ..":
        dir_struct["parent_dir"] = parent_dir.parent
        parent_dir = parent_dir.parent
        continue
    else:
        dir_struct["parent_dir"] = parent_dir
        parent_dir = parent_dir.joinpath(i[0].replace("cd ", ""))
    dir_struct["current_dir"] = i[0].replace("cd ", "")
    dir_struct["dirs"] = [item for item in i if is_dir(item)]
    # only storing the space of the sum of files
    dir_struct["files"] = sum([int(item.split(" ")[0]) for item in i if is_file(item)])

    result.append(dir_struct)


def calculate_dir_space(dir_struct):
    """
    Finding the totals of the dir by finding the subdirectory(s) whose parent directory starts with
    the combination of the parent dir and the current dir
    """
    parent_dir = dir_struct["parent_dir"].joinpath(dir_struct["current_dir"]).as_posix()
    total_sum = dir_struct["files"]
    for i in result:
        if i["parent_dir"].as_posix().startswith(parent_dir):
            total_sum = total_sum + i["files"]
    return total_sum


sum_of_dir_space = 0
for i in result:
    i["total_space"] = calculate_dir_space(i)
    if i["total_space"] < 100000:
        sum_of_dir_space = sum_of_dir_space + i["total_space"]

# task 1 result
print(sum_of_dir_space)

# task 2 (find the dir which needs to be deleted)
current_unused_space = 70000000 - result[0]["total_space"]
required_space = 30000000 - current_unused_space

b = [abs(required_space - i["total_space"]) for i in result]
# task 2 result
print(required_space + min(b))
