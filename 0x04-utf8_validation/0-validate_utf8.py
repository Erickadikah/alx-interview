#!/usr/bin/python3
""" This is method 2 of the UTF-8 Validation problem
    - This method is less efficient than method 1
    - This method usses hexadecimals instead of binary
    - to check if an integer is a valid UTF-8 character
    - in the int[data] being passed in
"""


def validUTF8(data):
    """
        Args: data[int]
        Each interger reprsents 1byte
        Return: True if data is a valid UTF-8 encoding,
        else return False
        0x80 = 10000000: 1 byte character: 128
        0xC0 = 11000000: 2 byte character: 192
        0xE0 = 11100000: 3 byte character: 224
        0xF0 = 11110000: 4 byte character: 240
        we are checking if the first byte is a valid UTF-8 character
        if it is, we check the next byte to see
          if it is a valid UTF-8 character
        in the case of a 3 byte character, we check the next 2 bytes
    """
    i = 0
    while i < len(data):
        if data[i] < 128:
            i += 1
        elif data[i] < 192:
            return False
        elif data[i] < 224:
            if i + 1 >= len(data) or (data[i + 1] & 192) != 128:
                return False
            i += 2
        elif data[i] < 240:
            if i + 2 >= len(data) or (data[i + 1] &
                                      192) != 128 or (data[i + 2] &
                                                      192) != 128:
                return False
            i += 3
        elif data[i] < 248:
            if i + 3 >= len(data) or (data[i + 1] & 192) != 128 or (
                    data[i + 2] & 192) != 128 or (data[i + 3] & 192) != 128:
                return False
            i += 4
        else:
            return False
    return True
