import re
import sys

conditions = sys.argv[1]
begin, close = conditions.split('-')

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).?\d{4}:(?P<hour>\d{2}):\d{2}.? ')
for line in sys.stdin:
  match = pat.search(line)
  if match and (int(match.group('hour')) >= int(begin) and int(match.group('hour')) < int(close)):
    print('%s\t%s'% (match.group('hour')+ '\t' +match.group('ip'), 1))
