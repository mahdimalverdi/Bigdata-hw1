#!/usr/bin/python3
import sys

def main(separator='\t'):
    lines = []
    read_header = False
    for line in sys.stdin.readlines():
        if not read_header:
            read_header = True
            continue

        lines.append('%s%s%d' % (line.split(',')[7], separator, 1))
    print('\n'.join(lines))

if __name__ == "__main__":
    main()
