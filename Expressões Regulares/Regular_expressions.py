import re
numlist = list()
file_name = input("Enter the name of the file")
if len(file_name)<1: file_name = "actual_data.txt"
fhandle = open(file_name, "r")
for line in fhandle:
    stuff = re.findall("[0-9]+", line)
    if len(stuff)<1: continue
    for n in stuff:
        print(n)
        num = float(n)
        numlist.append(num)
print(sum(numlist))