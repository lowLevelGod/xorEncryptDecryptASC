import sys

pwd = list(sys.argv[1])
infile = sys.argv[2]
outfile = sys.argv[3]

f = list(open(infile, "r").read())
o = open(outfile, "wb")

szpwd = len(pwd)
for i in range(len(f)):
    f[i] = chr(ord(f[i]) ^ ord(pwd[i % szpwd]))
    
o.write((''.join(x for x in f)).encode('charmap'))