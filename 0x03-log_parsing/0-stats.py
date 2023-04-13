#!/usr/bin/python3
"""this funtion reads stdin line by line and compute metrics
   input format :  <IP Address> -
    [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
"""
import sys


stdin = sys.stdin
counter = 0
total_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        404: 0,
        405: 0,
        500: 0}
try:
    for line in stdin:
        counter += 1
        status_code = int(line.split()[-2])
        if status_code in status_code_counts and len(line.split()) == 9:
            status_code_counts[status_code] += 1
            file_size = int(line.split()[-1])
            total_size += file_size
        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in status_code_counts.items():
                if count != 0:
                    print("{}: {}".format(code, count))
except KeyboardInterrupt as error:
    print("File size: {}".format(total_size))
    for code, count in status_code_counts.items():
        if count != 0:
            print("{}: {}".format(code, count))
