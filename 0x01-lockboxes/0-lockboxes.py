#!/usr/bin/python3

"""This is an interview Question called lockboxes that
checks to see if all boxes can be unlocked.

You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    stack = [0]
    visited = set(stack)

    while stack:
        idx = stack.pop()

        if idx >= len(boxes):
            visited.remove(idx)
            continue
        for j in boxes[idx]:
            if j not in visited:
                stack.append(j)
                visited.add(j)

    return len(visited) == len(boxes)