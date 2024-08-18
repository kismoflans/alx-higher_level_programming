#!/usr/bin/python3
# 101-stats.py
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1  # Reset count after printing stats
            else:
                count += 1

            line = line.split()

            if len(line) < 2:  # Check if line is too short
                continue

            try:
                size += int(line[-1])
            except ValueError:
                continue  # Skip lines where the size is not an integer

            if len(line) > 1 and line[-2] in valid_codes:
                status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1

        # Print the final statistics on exit
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
