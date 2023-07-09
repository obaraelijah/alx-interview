#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
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