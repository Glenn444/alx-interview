#!/usr/bin/python3
"""Lockboxes algorithm
Is a method that determines if all boxes can be opened

"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
