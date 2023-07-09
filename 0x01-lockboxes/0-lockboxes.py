#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened.
Given n number of locked boxes, each box numbered sequentially
from 0 to n - 1, and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    if not boxes or type(boxes) is not list:
        return False
    
    unlocked = [0] 
    
    for x in unlocked:
        for y in boxes[x]:
            if y not in unlocked and y < len(boxes):
                unlocked.append(y)
    
    # Check if all boxes are unlocked
    if len(unlocked) == len(boxes):
        return True
    return False
