import sys

pwd = list(sys.argv[2])
infile = sys.argv[1]
outfile = sys.argv[3]

f = list(open(infile, "rb").read())
o = open(outfile, "w")

szpwd = len(pwd)
for i in range(len(f)):
    f[i] = chr(ord(f[i]) ^ ord(pwd[i % szpwd]))
    
o.write(''.join(x for x in f)) 