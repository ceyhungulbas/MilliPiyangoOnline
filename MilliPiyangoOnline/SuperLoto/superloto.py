from collections import Counter
import re
import random
import itertools
import collections

numbers = []
jokernumber = []
_190sayilar = []

f = open('SuperLoto\superloto.txt')
lines = f.readlines()

#print(lines)



print("________________________________")

for line in lines:
    currentNumbers = line.split()
    for num in currentNumbers:
        numbers.append(int(num))

#print(numbers)



#Group elements
n = 6
groupwith6 = [numbers[k:k+n] for k in range(0, len(numbers), n)]


#sorted
sorted_numbers = numbers.sort()


numbers_butcounter = Counter(numbers)



print("________________________________")
print("________________________________")
print("________________________________")
print("________________________________") 
print("________________________________")




#Çekiliş sayısı ve o günkü değer
print("Çekiliş sonuçları")
for count, value in enumerate(groupwith6, start=1):
    print(count, value)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

tekrar_liste=[]
for _6li in groupwith6:
    for element in _6li:
        tekrar = numbers_butcounter[element]
        tekrar_liste.append(tekrar)
        print(_6li, "->", "{} sayısı {} kere çıktı.".format(element, tekrar))
    print("-----------------------")


print("________________________________")
print("6'lı sayılar\n")


print(numbers_butcounter.most_common())


tekrar_liste = Counter(tekrar_liste)
# print(tekrar_liste)


c = collections.Counter(numbers_butcounter)
#i = random.randrange(sum(c.values()))
# print("\n", c, "\n\n", c.keys() , "\n\n" ,c.values(),"\n\n")
# print(len(c.values()))
# print(len(c.keys()))
# print(type(c.values()))
# print(type(c))


# for e in c:
#     print("Key:",e,"Value:",c[e])

# print("__________________________________________")

a=[]

for e in c:
    if c[e]>5:
        # print("Key:",e,"Value:",c[e])
        a.append(e)

print(a)

print("__________________________________________")


randomlist = random.sample(a, 6)
randomlist.sort()



print("\nKuponunuz:", ', '.join(map(str,randomlist)))



print("\nBol şans")
input("\nSonlandırın.")