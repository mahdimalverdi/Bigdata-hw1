#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file):
    for line in file:
        yield line

def main(separator='\t'):
    lines = []
    data = read_mapper_output(sys.stdin)
    max_temps = {}
    min_temps = {}
    for line in data:
        try:
            date, temp = line.split(separator)
            temp = float(temp.strip('\n'))
            year = date[0: 6]
            if year in max_temps:
                if(max_temps[year][1] < temp):
                    max_temps[year] = (date,temp)
            else:
                max_temps[year] = (date,temp)
            if year in min_temps:
                if(min_temps[year][1] > temp):
                    min_temps[year] = (date,temp)
            else:
                min_temps[year] = (date,temp)
        except ValueError:
            pass
        
    for key in max_temps:
        print('%s%s%s' % (max_temps[key][0], separator, max_temps[key][1]))
        print('%s%s%s' % (min_temps[key][0], separator, min_temps[key][1]))

if __name__ == "__main__":
    main()
