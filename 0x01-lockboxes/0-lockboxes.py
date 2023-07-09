#!/usr/bin/python3

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # The first box is unlocked initially
    stack = [0]  # Use a stack to keep track of boxes to explore

    while stack:
        current_box = stack.pop()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
