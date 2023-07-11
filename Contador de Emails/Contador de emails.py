name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or not "From" in words:
        continue
    di[words[1]] = di.get(words[1],0)+1
largest_value = -1
largest_key = None
for k,v in di.items():
    if v>largest_value:
        largest_value = v
        largest_key = k
print(largest_key, largest_value)
