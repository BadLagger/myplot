import sys

file_path = sys.argv[1]
m = int(sys.argv[2])
n = int(sys.argv[3])

file = open(file_path, 'w')

import random
array = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.uniform(-100.0, 100.0))
        file.write(str(row[j]) + ' ')
    array.append(row)
    file.write('\n')

file.close()
    