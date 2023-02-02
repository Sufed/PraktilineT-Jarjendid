from random import *
#Harjutus 6. Проверка имени.
имя = input("Введите ваше имя: ")
if имя.isalpha():
    приветствие = "Здравствуйте " + имя.capitalize() + "!"
    print(приветствие)
    длина_имени = len(имя)
    print("В имени", длина_имени, "буквы.")
    гласные = "aeiouAEIOU"
    количество_гласных = 0
    количество_согласных = 0
    for i in имя:
        if i in гласные:
            количество_гласных += 1
        else:
            количество_согласных += 1
    print("В имени", количество_гласных, "гласные и",
          количество_согласных, "согласные.")
    отсортированное_имя = "".join(sorted(set(имя.lower())))
    print("Буквы в алфавитном порядке:", отсортированное_имя)
else:
    print("Неверное имя. Допускаются только буквы.")



#Harjutus 5.

#Harjutus 4. Сортировка.
print("Harjutus 4. Сортировка")
numbers = [4, -2, -1, 9, -8, 0]
numbers.sort()
print("Ascending: ", numbers)
numbers.sort(reverse=True)
print("Descending: ", numbers)

#Harjutus 3. Бесполезные числа. (1)
print("Harjutus 3. Бесполезные числа")
numbers=input("Введи числа через пробел: ").split()
#numbers=[1, 2, 3, 4, 5]
Большие=max(numbers) #Функция max() находить максимальное число.
Бесполезные=Большие/len(numbers) #Большое число делим на кол-во символов.
for i in range(len(numbers)): 
    if numbers[i] == Большие:
        numbers[i] = Бесполезные
print(numbers)
print()
print()
print()




#Harjutus 3. Бесполезные числа. (2)
print("Harjutus 3. Бесполезные числа")
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=max_arv/kogus
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)




#Harjutus 2. Перемена мест (1)
print("Harjutus 2. Перемена мест")
maakonnad=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa"]
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1):
        osa1.append(maakonnad[i])
    for j in range(n+1,len(maakonnad)+1): #n+1,....len()
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("Viga")
print()
print()
print()




#Harjutus 2. Перемена мест (2)
print("Harjutus 2. Перемена мест")
numbers =input("Вводи числа между которых пробелы: ").split()
print(numbers)
#numbers = [1, 2, 3, 4, 5]
n=int(input("Количество цифр которое хочешь поменять: "))
for i in range(n//2):
    numbers[i], numbers[-(i+1)] = numbers[-(i+1)], numbers[i]
print("Reverse: ", numbers)
print()
print()
print()




#Harjutus 1. Почтовый индекс
print("Harjutus 1. Почтовый индекс")
index=""
maakonnad=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa","Saaremaa"]
while True:
    try:
        index=int(input("Введите индекс: "))
        if index<99999 and index>10000:
            break
    except:
        print("Неправильный индекс.")
#index=str(index)
i=index//10000 #1,2,3,4,5,6,7,8,9...
print(f"{index} on {maakonnad[i-1]}") #0,1,2,3,4,5,6,7,8,9....
if i in [1,2,3]:
    print("Оставайтесь дома")
else:
    print("Носите маски")
