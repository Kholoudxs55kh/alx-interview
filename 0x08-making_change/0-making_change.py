#!/usr/bin/python3
"""_summary_
"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """
    if total <= 0 or len(coins) == 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for i in coins:
        count += total // i
        total = total % i
    if total != 0:
        return -1
    return count
