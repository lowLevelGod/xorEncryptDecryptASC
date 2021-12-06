import sys

infile = sys.argv[1]
outfile = sys.argv[2]

f = list(open(infile, "r").read())
o = list(open(outfile, "rb").read())

for i in range(15):
    print(chr(ord(f[i]) ^ o[i]), end ="")