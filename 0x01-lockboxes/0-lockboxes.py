#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    """checking the lenth of the boxes"""
    if(len(boxes) == 0 or type(boxes) != list):
        """initilization for unchecked boxes"""
        return false

    b_locked = len(boxes)
    keys = [0]
    for key in keys :
        for box in boxes[key]:
            if (box != 0 and box < b_locked):
                keys.append(box)


    keys = set(keys)

    if (len(keys) == len(boxes)):
        return True
    else:
        return False
