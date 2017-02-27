fi = open("in.txt","r")
k1 = fi.read(10)
print k1
pos = fi.tell()
print pos
k = fi.seek(2,2)
print fi.tell()
print fi.read(1)
