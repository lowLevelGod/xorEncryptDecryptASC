import sys

f = list(open(sys.argv[1], "rb").read())

for i in range(10, 16):
    freq = [[0] * 256 for x in range(i)]
    k = [-1] * i
    
    #print(freq)
    
    for j in range(len(f)):
        poz = j % i
        freq[poz][f[j]] += 1
        if freq[poz][f[j]] > freq[poz][k[poz]]:
            k[poz] = f[j]
    
    for j in range(i):
        k[j] = k[j] ^ 32
    
    print(''.join(chr(x) for x in k))
    
            