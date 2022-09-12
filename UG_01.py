from collections import Counter

def menghitung_kata(kal, kata):
    temp = Counter((kal.lower()).split())
    return temp[kata.lower()]

kal = input("Masukkan Kalimat : ")
kata = input("Masukkan kata yang dicari : ")
print(menghitung_kata(kal,kata))