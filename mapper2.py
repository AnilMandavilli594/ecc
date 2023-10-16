import sys
import re
search_hours = sys.argv[1]
start, end = search_hours.split('-')
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    line = line.strip()
    match = pat.search(line)
    if match and (int(match.group('hour')) >= int(start) and int(match.group('hour')) < int(end)):
        print('%s\t%s'% (match.group('hour')+ '\t' +match.group('ip'), 1))