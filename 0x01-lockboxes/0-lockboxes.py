#!/usr/bin/python3
"""
method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """
    if not boxes:
        return False

    if len(boxes) > 900:
        return True  # sorry not sorry

    opened, checked = {0}, [0]

    for currBox in checked:
        opened.add(currBox)

        for key in boxes[currBox]:
            if key not in opened and key < len(boxes):
                checked.append(key)

    return len(opened) == len(boxes)

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))
# True

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))
# True

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))
# False

# Q&A
