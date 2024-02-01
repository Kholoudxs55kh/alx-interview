#!/usr/bin/python3
"""task"""


def validUTF8(data):
    """
    anything
    """
    bytes_ = 0
    for i in data:
        byte = format(i, '#010b')[-8:]
        if bytes_ == 0:
            if byte[0] == '1':
                bytes_ = len(byte.split('0')[0])
            if bytes_ > 4 or bytes_ == 1:
                return False
            if bytes_ == 0:
                continue
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        bytes_ -= 1
    return bytes_ == 0
