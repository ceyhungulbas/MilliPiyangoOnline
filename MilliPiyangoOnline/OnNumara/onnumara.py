from collections import Counter
import re
import random

numbers = []
jokernumber = []
_190sayilar = []

f = open('OnNumara\onnumara.txt')
lines = f.readlines()

#print(lines)



print("________________________________")

for line in lines:
    currentNumbers = line.split()
    for num in currentNumbers:
        numbers.append(int(num))

#print(numbers)



#Group elements
n = 22
groupwith22 = [numbers[k:k+n] for k in range(0, len(numbers), n)]


#sorted
sorted_numbers = numbers.sort()


print("________________________________")
print("22'li sayılar\n")

numbers_butcounter = Counter(numbers)
print(numbers_butcounter.most_common())



print("________________________________")
print("________________________________")
print("________________________________")
print("________________________________") 
print("________________________________")




#Çekiliş sayısı ve o günkü değer
print("Çekiliş sonuçları")
for count, value in enumerate(groupwith22, start=1):
    print(count, value)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


for _22li in groupwith22:
    for element in _22li:
        tekrar = numbers_butcounter[element]
        print(_22li, "->", "{} sayısı {} kere çıktı.".format(element, tekrar))
    print("-----------------------")

        # print("Element:", element, "tekrar:",tekrar)
        #>>>Element: 3 tekrar: 3







# import random
# #Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(10, 30), 5)
# print(randomlist)





"""
-Bilgisayardan random kupon oluşturma
"""
print("\nYazılım öğrenseydin amcık")
# input("Sonlandırın.")