#!/usr/bin/python3
import sys

def main(separator='\t'):
    lines = []
    for line in sys.stdin.readlines():
        date =  line[6: 14]
        temp_max = float(line[38: 45])
        temp_min = float(line[46: 53])
        if (temp_max > 35.0) :
            lines.append("%s%s%d" % (date, separator, temp_max))
        if (temp_min < 10) :
            lines.append("%s%s%d" % (date, separator, temp_min))
    print('\n'.join(lines))

if __name__ == "__main__":
    main()
