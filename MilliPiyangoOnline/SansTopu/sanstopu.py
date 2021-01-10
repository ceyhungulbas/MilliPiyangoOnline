from collections import Counter
import re
import random
import itertools
import collections

numbers = []
jokernumber = []

f = open('SansTopu\sanstopu.txt')
lines = f.readlines()

print("________________________________")

for line in lines:
    currentNumbers = line.split()
    for num in currentNumbers:
        numbers.append(int(num))


#print(numbers)

n = 6
groupwith6 = [numbers[k:k+n] for k in range(0, len(numbers), n)]


print("________________________________")
print("Hem 5'li hem de Joker sayılar\n")

numbers_butcounter = Counter(numbers)
print(numbers_butcounter.most_common())



print("________________________________")
print("Joker Sayılar\n")

i=5
while i < len(numbers):
    jokernumber.append(numbers[i])
    i += 6

jokernumber_butcounter = Counter(jokernumber)
print(jokernumber_butcounter.most_common())



print("________________________________")
print("İlk 5'li sayılar\n")

numbers_butcounter1 = numbers_butcounter - jokernumber_butcounter
print(numbers_butcounter1.most_common())




#Çekiliş sayısı ve o günkü değer
print("Çekiliş sonuçları")
for count, value in enumerate(groupwith6, start=1):
    print(count, value)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for _6li in groupwith6:
    for element in _6li:
        tekrar = numbers_butcounter1[element]
        tekrarjoker = jokernumber_butcounter[element]
        print(_6li, "->", "{} sayısı {} kere çıktı. {} joker sayısı {} kere çıktı.".format(element, tekrar,element, tekrarjoker))
        # print(_6li, "->", "{} sayısı {} kere çıktı.".format(element, tekrarjoker))
    print("-----------------------")



print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


c = collections.Counter(numbers_butcounter)
j = collections.Counter(jokernumber_butcounter)

a=[]

for e in c:
    if c[e]>5:
        # print("Key:",e,"Value:",c[e])
        a.append(e)

#print(a)


aa=[]

for e in j:
    if j[e]>2:
        # print("Joker Key:",e," Joker Value:",j[e])
        aa.append(e)

#print(aa)

print("__________________________________________")


randomnumber = random.sample(a, 5)
randomnumber.sort()

randomjoker = random.sample(aa, 1)
randomlist = randomnumber + randomjoker



print("\nKuponunuz:", ', '.join(map(str,randomlist)))



print("\nBol şans")
input("\nSonlandırın.")