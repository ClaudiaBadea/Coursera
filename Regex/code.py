import re
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
numlist = list()
total = 0
count = 0

for line in handle:
    line = line.rstrip()
    numbs = re.findall('\d+(?:\.\d+)?', line)
    for num in numbs:
        if num in numlist:
            continue
        numlist.append(num)
        fnum = float(numlist[0+count])
        count = count+1
        total = total + fnum
print(total)
