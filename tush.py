import re
from collections import defaultdict

def process_log(log):
    ip_counter = defaultdict(list)
    status_counter = defaultdict(int)
    total_count = 0
    for m in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - .*?HTTP/1.1" (\d+) (\d+)', log):
        total_count += 1
        ip = m[1]
        status = m[2]
        bytes = int(m[3])
        ip_counter[(ip, status)].append(bytes)
        status_counter[status] += 1
    for k, v in ip_counter.items():
        count = len(v)
        total_bytes = sum(v)
        ip = k[0]
        status = k[1]
        
    for k, v in status_counter.items():
        count = v
        print(f"Status Code {k} -> Count {count}")
        
str1 = open('log', 'r').read()
process_log(str1)
