#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Args: data[int]
        Reurns: True if data is a valid UTF-8 encoding,
        else return False
        '>>' is the bitwise right shift operator
        shifting the bits of the number to the right
        resulsting to a new byte where MSB is still 0
        resulting to true if the number is 0
        byte_number: keep track of the number of bytes
        in the current UTF-8 character
    """
    bytes_number = 0
    for byte in data:
        if bytes_number == 0:
            if ( byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                bytes_number = 1
            elif (byte >> 4) == 0b1110:
                bytes_number = 2
            elif (byte >> 3) == 0b11110:
                bytes_number = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_number -= 1
    return bytes_number == 0