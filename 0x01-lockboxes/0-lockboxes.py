#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    """checking the lenth of the boxes"""
    n = len(boxes)
    b_unlocked = [0]
    for  box_num, box in enumerate(boxes):
        for key in box:
            if key < n and key not in b_unlocked and key != box_num:
                b_unlocked.append(key)

    return len(b_unlocked) == n
