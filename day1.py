with open("day1.txt") as f:
    """
    Reading the txt file of inputs and parsing them in a way such that I can create a list of lists
    Each sublist within the list will represent the list of calories of a single elf
    """
    lines = f.readlines()
    lines = "".join([i.replace("\n", " ") if i != "\n" else i for i in lines])

    # splitting on '\n' will create a list where each element is a string of numbers separated by ' '
    lines = lines.split("\n")

    # splitting on ' ' will create the a list of lists where each sublist is the no. of cals for each elf
    lines = [i.split() for i in lines]
    lines = [[int(j) for j in i] for i in lines]  # converting to int
    lines = [sum(i) for i in lines]
    print(f"Most calories - {max(lines)}")  # answer 1

    print(f"Sum of top 3 - {sum(sorted(lines, reverse=True)[0:3])}")  # answer 2
