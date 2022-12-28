import hashlib
import struct
import math
from input_data import test_data

a_m = 0.697

def binary(n):
    if n == 0:
        return '0'
    else:
        return binary(n // 2) + str(n % 2)


def zero_counting(n, max_width): # functia care face diferenta de biti descrisa mai jos
    count = max_width - n.bit_length() + 1
    print("max_width", max_width)
    return count


class Hyperloglog:
    def __init__(self, b=5):
        self.b = b # numarul de biti alocati, in dependenta la asta vom alege numarul de registre
        self.reg = [0] * (1 << b)  # alocoam spatiu pentru numarul de registre
        self.register_size = 1 << b # numarul de registre 2^b



    def add(self, value):
        value = value.encode('utf-8')
        x = struct.unpack('!Q', hashlib.sha1(value).digest()[:8])[0] # asta e valoarea hashata

        j = x & (self.register_size - 1) # indexul registrului
        w = x >> self.b # restul numarului fara biti pentru index

        """""
        deci noi mai intai hasham valoarea in >> x, care este pus in baza 16.
        apoi facem bitwise AND operation ca sa aflam cu ce sunt egali primii b biti, cei care is responsabili pentru index
        In w, lasam restul bitului.
        
        ca sa aflam streak-ul de zerouri, nu le numaram, dar ce facem:
        luam marimea normala a unui bit (noi stim ca e 64), scadem din 64 cei b biti alocati pentru index.
        deci in toerie, ar trebui sa avem 64-b biti, dar deoarece in binar, cand un numar se incepe cu 0, acel 0 nu se scrie,
        pai noi din diferenta aceasta aflam acei 0-uri care au fost neglijati.
        """""

        self.reg[j] = max(self.reg[j], zero_counting(w, 64 - self.b))
        # punem in registru countul, updatandul daca este mai mare ca cel curent




        print("j=", j)
        print("w =", bin(w))
        print("count =", zero_counting(w, 64 - self.b))








hll = Hyperloglog(b=5)


k = 0


for i in test_data:
    k += 1
    hll.add(i)

l = 1
for i in hll.reg:
    print("m[{}]=".format(l), i)
    l += 1

E = a_m * float(hll.register_size ** 2) / sum(math.pow(2.0, -x) for x in hll.reg)

print(k)
print("E = ", E)












