# --- Day 5: Supply Stacks ---
"""
Current stack of crates given on top, instructions to move given below.
Example - 
move 1 from 2 to 1 - (move 1 crate from stack no. 2 to stack no.1)

After the rearrangement procedure completes, what crate ends up on top of each stack?
Note - For task 1 each crate from the stack is moved one at a time, 
For task 2 the entire crate stack is moved at once.
"""
with open("day5.txt") as f:
    lines = f.readlines()

    current_stacks = [i for i in lines if "move" not in i]
    move_instructions = [i for i in lines if "move" in i]

# parsing the stacks into a list (essentially doing all of this to retain only the letters, no crate represented by blanks)
current_stacks = [i.replace("    ", " [ ]").replace("\n", "") for i in current_stacks]
current_stacks = [
    i.replace(" ", "").replace("[]", "[ ]") for i in current_stacks if "[" in i
]
current_stacks = [i.replace("[", "").replace("]", "") for i in current_stacks]


def parse_stacks(current_stacks):
    """
    Looping thru the input list in reverse and assigning the letters to a dict where the
    key represents the stack number and the values are the crates
    """
    current_stacks_dict = {}
    for stack_row in reversed(current_stacks):
        for ind, item in enumerate(stack_row):

            current_stacks_dict[
                ind + 1
            ] = f"{current_stacks_dict.get(ind + 1, '')}{stack_row[ind]}"

    # removing spaces from the final dict
    current_stacks_dict = {
        k: v.replace(" ", "") for k, v in current_stacks_dict.items()
    }
    return current_stacks_dict


def parse_moves(move_instructions):
    """
    Retaining the three numbers from the instructions
    """
    move_instructions = [
        [int(j) for j in i.split() if j.isdigit()] for i in move_instructions
    ]
    return move_instructions


parsed_current_stacks = parse_stacks(current_stacks)
move_instructions = parse_moves(move_instructions)


def get_result(task_number=1):
    """
    Performs the actual task of moving crates as described in the move_instructions
    Note - the argument represents the task number (1 or 2, 1 by default)
    """
    for limit, i in enumerate(move_instructions):
        move, from_stack, to_stack = i
        parsed_current_stacks[from_stack], blocks = (
            parsed_current_stacks[from_stack][:-move],
            parsed_current_stacks[from_stack][-move:],
        )
        if task_number == 1:
            # reversing the block order since the blocks are moved one at a time the one at the top will end up at the bottom
            parsed_current_stacks[to_stack] = (
                parsed_current_stacks[to_stack] + blocks[::-1]
            )
        if task_number == 2:
            parsed_current_stacks[to_stack] = parsed_current_stacks[to_stack] + blocks

    return parsed_current_stacks


task1_result = "".join([i[-1] for i in get_result(task_number=1).values()])
# the below is required because the existing parsed_current_stacks var gets changed when we run the function (look for another way to do this part)
parsed_current_stacks = parse_stacks(current_stacks)

task2_result = "".join([i[-1] for i in get_result(task_number=2).values()])
print(f"Task 1 result - {task1_result}")
print(f"Task 2 result - {task2_result}")
