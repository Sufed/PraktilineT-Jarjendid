#Harjutus 3. Бесполезные числа.
print("Harjutus 3. Бесполезные числа")
numbers=[1, 2, 3, 4, 5]
Большие=max(numbers) #Функция max() находить максимальное число.
Бесполезные=Большие/len(numbers) #Большое число делим на кол-во символов.
for i in range(len(numbers)): 
    if numbers[i] == Большие:
        numbers[i] = Бесполезные
print(numbers)
print()
print()
print()




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
