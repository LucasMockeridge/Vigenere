import random 

def sub(key, string):
    out = [None] * len(string)
    for i in range(len(string)):
        ch = string[i]
        out[i] = key[ord(ch)-97]
    return ''.join(out)

def getVal(a, b):
    return chr((ord(a) + ord(b) - 193) % 26 + 97)

def vigenere(key, string):
    out = ""
    for i in range(len(key)):
        out += getVal(key[i], string[i])
    return out

def subKeys(alpha):
    keys = []
    while len(keys) < 10:
        tmp = alpha.copy()
        random.shuffle(tmp)
        string = ''.join(tmp)
        if string not in keys:
            keys.append(string)
    return keys

def vigKeys(alpha, length):
    keys = []
    while len(keys) < 10:
        key = ''.join(random.choice(alpha) for x in range(length))
        if key not in keys:
            keys.append(key)
    return keys

def encrypt(m, vk, sk):
    pt = m
    for i in range(10):
        pt = vigenere(vk[i],sub(sk[i],pt))
    return pt 

def formTable(alpha, vk, sk, length):
    table = [{}] * length
    for i in alpha:
        c = encrypt(i * length, vk, sk)
        for j in range(length):
            entry = {i : c[j]}
            table[j] = {**table[j], **entry}
    return table

def tableEncrypt(m, table):
    c = ""
    for i in range(len(m)):
        c += table[i][m[i]]
    return c

def tableDecrypt(c, table):
    m = ""
    for i in range(len(c)):
        d = table[i]
        m += list(filter(lambda x: d[x] == c[i], d))[0]
    return m

def main():
    m = input("Enter a message (lowercase letters only): ")
    length = len(m)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vk = vigKeys(alpha, length)
    sk = subKeys(alpha)
    table = formTable(alpha,vk,sk,length)
    c = encrypt(m, vk, sk)
    print("Encrypted: " + c)
    print("Decrypted: " + tableDecrypt(c, table))
   
if __name__ == '__main__':
    main()
