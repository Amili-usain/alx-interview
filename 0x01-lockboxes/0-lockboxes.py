#!/usr/bin/python3
"""lockbox challenge"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    num_boxes = len(boxes)
    unlocked_boxes = set([0])   # starts with the first box unlocked
    keys = set(boxes[0])   # collects keys from the first box
    while keys:
        key = keys.pop()
        if key < num_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])
    return len(unlocked_boxes) == num_boxes
