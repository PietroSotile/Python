name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words)<3 or not "From" in words:
        continue
    tempo = words[5].split(":")
    di[tempo[0]] = di.get(tempo[0],0)+1
x = sorted(di.items())
#print(x)
for k,v in x:
    print(k,v)