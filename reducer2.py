import sys
from collections import defaultdict
dict_ip_count = defaultdict(lambda: defaultdict(int))
for line in sys.stdin:
    line = line.strip()
    hour, ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[hour][ip] += int(num)
    except ValueError:
        pass
for tmp in dict_ip_count:
    sorted_dict_ip_count = sorted(dict_ip_count[tmp],
key=dict_ip_count[tmp].get, reverse=True)[:3]
    for key in sorted_dict_ip_count:
        print ('%s\t%s\t%s' % (tmp, key, dict_ip_count[tmp][key]))