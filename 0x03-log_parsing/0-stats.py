#!/usr/bin/python3
"""this funtion reads stdin line by line and compute metrics
   input format :  <IP Address> -
    [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
"""
import sys


def process_logs(log_lines):
    counter = 0
    total_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    for line in log_lines:
        counter += 1
        status_code, file_size = parse_log_line(line)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        total_size += file_size
        if counter % 10 == 0:
            counter = 0
            print_stats(total_size, status_code_counts)
    print_stats(total_size, status_code_counts)


def parse_log_line(line):
    """ pass a line with a format:
      <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>
    if the line is not with the above format returns None
    """
    fields = line.split()
    status_code = int(fields[-2])
    file_size = int(fields[-1])
    return status_code, file_size


def print_stats(total_size, status_code_counts):
    """
    prints the status
    """
    print("File size: {}".format(total_size))
    for code, count in status_code_counts.items():
        if count != 0:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    stdin = sys.stdin
    try:
        process_logs(stdin)
    except KeyboardInterrupt as error:
        process_logs(stdin)
