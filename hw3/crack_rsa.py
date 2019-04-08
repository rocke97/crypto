from itertools import count
from string import ascii_lowercase
import math

def find_factor(n):
    start = math.floor(math.sqrt(n))
    if start % 2 == 0:
        start = start - 1
    ans = 1
    while ans != 0:
        ans = n % start
        print(ans)
        if ans == 0:
            break
        start = start + 2
    return start

def multiplicative_inverse(a,b):
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    q = math.floor(a_0/b_0)
    r = a_0 - (q * b_0)
    while r > 0:
        temp = (t_0 - (q * t)) % a
        t_0 = t
        t = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q * b_0)
    return t

def sam(x, c, n):
    c = int(c)
    c = '{0:b}'.format(c) #to binary
    z = 1
    l = len(c)
    for i in range(l):
        z = (math.pow(z, 2)) % n
        if(c[i] == "1"):
            z = (z*x) % n
    return z

def decrypt_numbers(cipher):
    first = math.floor((cipher/(26*26))) % 26
    second = math.floor((cipher/26)) % 26
    third = math.floor(cipher) % 26
    return numbers_to_letters[first] + numbers_to_letters[second] + numbers_to_letters[third]    

numbers_to_letters = dict(zip(count(0), ascii_lowercase))
n = 31313
b = 4913
cipher_text = [
    6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809,
    23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395,
    27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881,
    25774, 7647, 23901, 7372, 25774, 18436, 12056, 13547,
    7908, 8635, 2149, 1908, 22076, 7372, 8686, 1304,
    4082, 11803, 5314, 107, 7359, 22470, 7372, 22827,
    15698, 30317, 4685, 14696, 30388, 8671, 29956, 15705,
    1417, 26905, 25809, 28347, 26277, 7897, 20240, 21519,
    12437, 1108, 27106, 18743, 24144, 10685, 25234, 30155,
    23005, 8267, 9917, 7994, 9694, 2149, 10042, 27705,
    15930, 29748, 8635, 23645, 11738, 24591, 20240, 27212,
    27486, 9741, 2149, 29329, 2149, 5501, 14015, 30155,
    18154, 22319, 27705, 20321, 23254, 13624, 3249, 5443,
    2149, 16975, 16087, 14600, 27705, 19386, 7325, 26277,
    19554, 23614, 7553, 4734, 8091, 23973, 14015, 107,
    3183, 17347, 25234, 4595, 21498, 6360, 19837, 8463,
    6000, 31280, 29413, 2066, 369, 23204, 8425, 7792,
    25973, 4477, 30989
]

p = find_factor(n)
print(p)
q = math.floor(n/p)

phi_n = (p-1) * (q-1)
a = multiplicative_inverse(phi_n, b)
plain_text_numbers = [sam(c, a, n) for c in cipher_text]
plain_text = [decrypt_numbers(c) for c in plain_text_numbers]
print (plain_text)


