# UTF-8 Validation

## Description

UTF-8 validation refers to the process of checking whether a given sequence of bytes conforms to the rules of the UTF-8 encoding scheme or not. UTF-8 is a variable-length encoding scheme for representing Unicode characters using 8-bit bytes. In UTF-8, characters can be encoded using 1 to 4 bytes, depending on the character code point.

The following rules apply to UTF-8 encoding:

- For a 1-byte character, the first bit must be a 0, followed by its Unicode code.
- For an n-byte character, the first n-bits must all be 1's, the n+1 bit must be 0, followed by n-1 bytes with most significant 2 bits being 10.

This means that for a two-byte character, the first byte starts with 110, followed by 5 bits of its Unicode code. The second byte starts with 10, followed by 6 bits of its Unicode code. This is illustrated in the following example:

```

Byte 1   | Byte 2   | Byte 3   | Byte 4
-------- | -------- | -------- | --------
110XXXXX | 10XXXXXX | 110XXXXX | 10XXXXXX

```

Given an array of integers representing the data, return whether it is a valid UTF-8 encoding.

## Example

```python
data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.

The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
```python

## Tasks

### 0. UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Author
ERICK ADIKAH