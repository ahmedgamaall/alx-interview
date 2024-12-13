#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """a method that determines if a given data set represents a valid
    UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer"""

    bytes_count = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if bytes_count == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                bytes_count += 1
            if bytes_count == 0:
                continue
            if bytes_count == 1 or bytes_count > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        bytes_count -= 1
    return bytes_count == 0
