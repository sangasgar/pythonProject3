# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1
list = [1, 2, "дом", 2.1, False, [1, 2, 2]]

for i in list:
    print(type(i))
#2
element_count = int(input("Введите количество элементов списка "))
my_list1 = []
i = 0
element = 0
while i < element_count:
    my_list1.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list1)/2)):
        my_list1[element], my_list1[element + 1] = my_list1[element + 1], my_list1[element]
        element += 2
print(my_list1)
# 3
listWeather = ["Зима", "Весна", "Лето", "Осень"]

inputWeatherNum = int(input("Введите номер месяца "))
if inputWeatherNum > 0 and inputWeatherNum < 3 or inputWeatherNum > 11:
    print(f"Время года {listWeather[0]}")
elif inputWeatherNum > 2 and inputWeatherNum < 6:
    print(f"Время года {listWeather[1]}")
elif inputWeatherNum > 5 and inputWeatherNum < 9:
    print(f"Время года {listWeather[2]}")
elif inputWeatherNum > 8 and inputWeatherNum < 12:
    print(f"Время года {listWeather[3]}")

listWeatherDict = {1: "Зима",
                   2: "Зима",
                   3: "Весна",
                   4: "Весна",
                   5: "Весна",
                   6: "Июнь",
                   7: "Июнь",
                   8: "Июнь",
                   9: "Осень",
                   10: "Осень",
                   11: "Осень", }
for k, v in listWeatherDict.items():
    if inputWeatherNum == k:
        print(f"Время года {v}")
# 4
listWordInput = (input("Введите слова через пробел ")).split(" ")
count = 1
for i in listWordInput:
    print(f"{count} - {i[:10]}")
    count = count + 1

# 5
my_list = [7, 5, 3, 3, 2]
inputUserNumber = int(input("Введите число "))
count_num = 0
for i in my_list:
    if inputUserNumber > i:
        my_list.insert(count_num, inputUserNumber)
        break
    elif inputUserNumber == i:
        my_list.insert(count_num, inputUserNumber)
        break
    elif count_num == len(my_list):
        my_list.append(inputUserNumber)
        break
    else:
        count_num = count_num + 1
        continue
print(my_list)
# 6
my_product = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "компьютер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "компьютер", "цена": 2000, "количество": 7, "eд": "шт."})
]
nameProduct = input("Введите название товара ")
priceProduct = int(input("Введите цену товара "))
countProduct = int(input("Введите количество товара "))

my_product.append(
    (len(my_product) + 1, {"название": nameProduct, "цена": priceProduct, "количество": countProduct, "eд": "шт."}))
print(my_product)

output_dict = dict({})
for product in my_product:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:

            
            output_dict.update({key: [value]})


print(f'собрана аналитика: {output_dict}')