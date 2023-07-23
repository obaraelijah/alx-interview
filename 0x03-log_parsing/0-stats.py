#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:m"""
import sys


def print_status_codes(status_codes):
    """Prints the status code with its count.
    Format:
        <status>: <count>
    """
    for key, val in sorted(status_codes.items()):
        print("{}: {}".format(key, val))


code = {}
total = 0
vals_total = 0

try:
    for line in sys.stdin:
        line_arr = line.split(" ")

        if len(line_arr) > 4:
            file_size = int(line_arr[-1])
            status = line_arr[-2]

            if status not in code:
                code[status] = 1
            else:
                code[status] += 1

            total += file_size
            vals_total += 1

        if vals_total == 10:
            vals_total = 0
            print("File size: {}".format(total))
            print_status_codes(code)

except Exception:
    pass

finally:
    print("File size: {}".format(total))
    print_status_codes(code)