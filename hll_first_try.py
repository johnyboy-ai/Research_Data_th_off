import hashlib

def binary(self):
    return bin(eval(self))

#55 elemente
test_data = {"csl", "mwy", "nkt", "xqu", "fbr", "swz", "vph", "lzo", "ktq", "pjc", "vxu", "dhr", "psm", "jik", "lrf",
             "zxc", "ybd", "owg", "hte", "zpu", "csf", "gya", "fkr", "axm", "wmz", "gby", "nlp", "ovj", "ice", "hbm",
             "vjq", "nqr", "ulc", "rxy", "kzd", "pbo", "yxq", "vws", "qat", "rmn", "gfe", "jky", "xsl", "bwi", "ujc",
             "dvz", "hox", "ftg", "bpc", "wkl", "xjy", "uis", "nrm", "vzb", "pah", "tjx"}


k = 0


for i in test_data:
    print(k, i)
    result = hashlib.sha256(i.encode())
    result = result.hexdigest() #resultatul hashat in baza 16

    result = bin(int(result, 16)) # rezultatul in baza 2
    print(result)

    indx = int(result[3])*2 + int(result[4]) * 1
    print(indx)
    print(result[3], result[4])

    k += 1


# b = 2
# m = 2^b => m = 4

registry_m = [0, 0, 0, 0]


