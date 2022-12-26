import hashlib
import math


a_m = 0.673


#281 elemente
test_data = {"25UvU", "QHSr9", "bMv1w", "bQRpK", "F6qoP", "7mZbm", "uHhLl", "N7yNE", "CdDZd", "xyNo2", "LOjYy", "2KDm8",
             "rzhpi", "dIbFa", "90wbH", "Qd9AF", "zH9O9", "splWF", "8G9AZ", "rpQ3G", "DuRYq", "iLE94", "vQN4Z", "iRT5q",
             "0iA9W", "BX3Pm", "SJJry", "3IqGV", "UN0mk", "wdfSr", "Oo1M7", "ys6nv", "Nu5an", "Pl5KC", "wIFN4", "YtMxk",
             "zZudH", "GET2V", "ZfYWy", "B77jl", "4aVxu", "9czjW", "bwSv3", "cbtqh", "wUV9h", "ICuys", "IbjfU", "mXjXf",
             "mVZ1g", "Q8q4i", "p7Io0", "kwYpn", "TuN2h", "ty2oM", "ifqhZ", "yVTa4", "vdxFV", "ueMhG", "4a081", "WLZbT",
             "NuvFZ", "LPShi", "m10oD", "n1eN4", "pAULt", "kH0hw", "Oj9be", "ndgsv", "5Gp4S", "IMani", "dT5uv", "yB8Lr",
             "ICPuf", "clMNP", "d4GD0", "ctJ6T", "2MvI8", "skh7n", "a4BiU", "sjtsZ", "IR1oA", "2GQwO", "F6QG1", "T9tjP",
             "AkPcb", "RCBsZ", "mF1Et", "6xfVw", "7lhpP", "yNgG8", "REPHq", "pYaZk", "1w4Di", "Qtq1C", "Q8tRx", "OE57w",
             "UUDTs", "14Vqw", "5wdwW", "18RSM", "km4sk", "PzKNp", "GZIXP", "rhnBX", "J8vpy", "689ZH", "34l7z", "eFaE4",
             "aii76", "x0Fq6", "GOxPq", "6jn52", "6kShn", "HWEMq", "F39rE", "5aMQS", "Vg1ie", "7h7FO", "ogBJJ", "2exwe",
             "3q51A", "e4DKg", "s1wr5", "rZ0X8", "8mWzS", "xXZ6R", "7oNVM", "NzVtR", "50sUQ", "z87dc", "2J2DJ", "LvTRL",
             "9RkEy", "3PmFW", "qINOW", "5g1Ar", "ssVh5", "J6Gv8", "ygbAA", "SSF0j", "nNfLp", "V9Tat", "4fJeE", "JSZ0Z",
             "nnX5g", "do2Rv", "3id1Q", "1lImY", "TiKpL", "Dtu44", "5SrsU", "qlOLS", "2aQYK", "QKk2i", "g1GE9", "fqRtf",
             "cEU7N", "XTAGd", "N4Su9", "Hg24E", "1ZyZs", "7Bn98", "br7rt", "pMOHH", "J7ufC", "YxF4n", "fmeAv", "lo9pj",
             "oMgo5", "00dgf", "TbVPA", "z7tOz", "YaaZp", "A18Nl", "VT1Ij", "SeiFC", "WoveL", "zVv2L", "QcUUz", "Mx8VZ",
             "EJSHA", "cIJ8Z", "CnWFA", "lnJu7", "PgQdG", "T0xcl", "tH5EP", "pgnAX", "Peurt", "Sm5sg", "HB4bJ", "KZ6cI",
             "kREoV", "rwCyc", "AuGn8", "3uUfU", "cdHTR", "boeM5", "0fs2G", "GJjXZ", "zulWM", "KR4ix", "AaZGm", "K0aBW",
             "272vw", "olAlc", "2ce3O", "robWE", "4BMu0", "ernQm", "CvB9L", "UwBvQ", "gqQDL", "xIDgQ", "FB9x8", "n3uQL",
             "6iNNz", "fzwjP", "D8fle", "JeYGT", "FCm3t", "6XXpW", "b3EkR", "Ene0t", "lfYYR", "ZE2S6", "c0P6N", "z9L0n",
             "TTVIt", "nm1vu", "RRfN2", "YtBuc", "7pK4J", "JDccu", "b8I2v", "0ffIJ", "iIgRV", "C5tyd", "ridRU", "2GzvX",
             "AVp5D", "zkgEC", "1MxRT", "emgqa", "UFnS3", "NHqHm", "6UcOq", "qZTUh", "HBsGu", "bNDCr", "TyY6V", "kDaw5",
             "wkanM", "yTfMQ", "e4Bun", "9cJVQ", "eG4UP", "S5Sy8", "a2J6f", "MWAdQ", "jM0Dx", "bUVbX", "v5f2R", "C3szW",
             "lOUMp", "dfn25", "h3J1m", "P7iW2", "f2E3d", "S6jG9", "3Q4XC", "kUU8l", "3rdMd", "Skoqq", "jJITb", "74pZW",
             "Fy4pN", "NRKTP", "bWw9A", "pNbdu", "EzSws", "mWd9H", "cMFsP", "DyYv5", "YpsLu", "fcqmo", "gdn4W", "ljLJP",
             "Jk13F", "NRxyJ", "wP3Gc", "QxUsk", "PrGao", "fJDAZ", "zdGZb", "Gq8hf", "3Vfnc", "eY1TP", "ewHex", "xlIoJ",}


k = 0
# b = 2
# m = 2^b => m = 4

registry_m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(len(test_data))


for i in test_data:
    print()
    print(k, i)
    result = hashlib.sha512(i.encode())
    result = result.hexdigest() #resultatul hashat in baza 16

    result = bin(int(result, 16)) # rezultatul in baza 2
    print(result)

    indx = int(result[3]) * 8 + int(result[4]) * 4 + int(result[5])*2 + int(result[6]) * 1
    print("index =", indx)
    print("biti indx:", result[3], result[4], result[5], result[6])

    k += 1

    length = len(result)
    print("s_lenght = ", length)
    l = 0

    while(result[length-1] != '1'):
        l += 1
        length -= 1

    print("l =", l)
    if(l > registry_m[indx]) :
        registry_m[indx] = l


Z = 0
k = 0


for i in registry_m:
    print("m[] =", i)
    Z += 1 / (pow(2, registry_m[k]))
    k += 1





print("summ = ", Z)
Final_r = a_m * 256 / Z

print("Final:", Final_r)


