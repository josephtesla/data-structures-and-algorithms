def jumpingOnClouds(c):
    # Write your code here
    # simple greedy algorithm
    position = 0
    min_jumps = 0
    end = len(c) - 1
    while position != end:
        if position + 2 <= end and c[position + 2] == 0:
            position = position + 2
        else:
            position = position + 1

        min_jumps += 1

    return min_jumps


