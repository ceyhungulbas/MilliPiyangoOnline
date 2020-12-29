from collections import Counter
import re
import random

numbers = []
jokernumber = []
_190sayilar = []

f = open('Sayisal\sayisal.txt')
lines = f.readlines()

#print(lines)



print("________________________________")

for line in lines:
    currentNumbers = line.split()
    for num in currentNumbers:
        numbers.append(int(num))

#print(numbers)



#Group elements
n = 7
groupwith7 = [numbers[k:k+n] for k in range(0, len(numbers), n)]


#sorted
sorted_numbers = numbers.sort()


#print("________________________________")
#Length of numbers
#print("Toplam sayı", len(numbers))


#print("________________________________")
#Kaç tane sayı kaç kere çıktı
# for i in range(91):
#     print("i = " + str(i))
#     print("Kaç tane var: ", numbers.count(i))
#     print("----------------------")



print("________________________________")
print("Hem 6'lı hem de Joker sayılar\n")

numbers_butcounter = Counter(numbers)
print(numbers_butcounter.most_common())



print("________________________________")
print("Joker Sayılar\n")

i=0
while i < len(numbers):
    jokernumber.append(numbers[i])
    i += 6

jokernumber_butcounter = Counter(jokernumber)
print(jokernumber_butcounter.most_common())



print("________________________________")
print("İlk 6'lı sayılar\n")

numbers_butcounter1 = numbers_butcounter - jokernumber_butcounter
print(numbers_butcounter1.most_common())

print("________________________________")
print("________________________________")
print("________________________________")
print("________________________________") 
print("________________________________")




#Çekiliş sayısı ve o günkü değer
print("Çekiliş sonuçları")
for count, value in enumerate(groupwith7, start=1):
    print(count, value)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")



tekrar_liste=[]
for _7li in groupwith7:
    for element in _7li:
        tekrar = numbers_butcounter[element]
        tekrar_liste.append(tekrar)
        print(_7li, "->", "{} sayısı {} kere çıktı.".format(element, tekrar))
    print("-----------------------")
    
# for _7li in groupwith7:
#     for element in _7li:
#         tekrar = numbers_butcounter[element]
#         tekrar_liste.append(tekrar)
#         print( "{}".format( tekrar))
#     print("-----------------------")
        # print("Element:", element, "tekrar:",tekrar)
        #>>>Element: 3 tekrar: 3

print("__________________________________________")

tekrar_liste = Counter(tekrar_liste)
print(tekrar_liste)




# import random
# #Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(10, 30), 5)
# print(randomlist)




# liste = [r,o,y,g,b,p,m,u]
# print("Renklerin listesi: \n\n", liste)
# liste2 = random.sample(liste, 4)


"""
-Bilgisayardan random kupon oluşturma
"""
print("\nYazılım öğrenseydin amcık")
# input("Sonlandırın.")