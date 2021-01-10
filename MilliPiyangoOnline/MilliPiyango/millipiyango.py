from collections import Counter
import re
import random

numbers = []
jokernumber = []
_190sayilar = []

f = open('MilliPiyango\millipiyango.txt')
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



print("________________________________")
print("6'lı sayılar\n")

numbers_butcounter = Counter(numbers)
print(numbers_butcounter.most_common())


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

for _6li in groupwith6:
    for element in _6li:
        tekrar = numbers_butcounter[element]
        print(_6li, "->", "{} sayısı {} kere çıktı.".format(element, tekrar))
    print("-----------------------")

        # print("Element:", element, "tekrar:",tekrar)
        #>>>Element: 3 tekrar: 3



input("\nSonlandırın.")