import collections
import csv
import sys

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
    out_csv = csv.writer(out)
    out_csv.writerow(['word', 'count'])
    words = []
    for line in f:
        words.extend(line.split())

    count = collections.Counter(words)
    for k, v in count.most_common():
        out_csv.writerow([k, v])
