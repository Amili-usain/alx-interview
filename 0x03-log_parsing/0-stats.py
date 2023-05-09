#!/usr/bin/env python3

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("Total file size: {}".format(log["total_file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[(.+)\] '
                       r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

    line_count = 0
    log = {}
    log["total_file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                ip_address = match.group(1)
                date = match.group(2)
                status_code = match.group(3)
                file_size = int(match.group(4))

                # Total file size
                log["total_file_size"] += file_size

                # Status code
                if status_code.isdecimal():
                    log["code_frequency"][status_code] += 1

                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        output(log)
