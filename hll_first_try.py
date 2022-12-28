import hashlib
import math
import fileinput
import input_data

a_m = 0.697




counter_elements = 0
# b = 4
# m = 2^b => m = 16

registry_m = [0] * 32
a_m = 0.7213 / (1 + 1.079 / 32)

for element in input_data.test_data:
    result = hashlib.sha1(element.encode()).hexdigest()

    result = bin(int(result, 16))
    counter_elements += 1

    indx = (int(result[3]) * 16 + int(result[4]) * 8 + int(result[5]) * 4 + int(result[6]) * 2 + int(result[7]) * 1)
    length = len(result) - 1
    l = 1

    while result[length] != '1':
        l += 1
        length -= 1

    registry_m[indx] = max(l, registry_m[indx])

for i in registry_m:
    print("M[]=", i)

print(counter_elements)
Final_r = a_m * float(32 ** 2) / sum(math.pow(2.0, -i) for i in registry_m)
print("Final:", Final_r)
