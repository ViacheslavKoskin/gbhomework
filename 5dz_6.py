import re

subs_total_hours = {}

with open("text_6.txt") as f:
    for line in f.readlines():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(subs_total_hours)