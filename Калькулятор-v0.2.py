import math
print("##################\n#Калькулятор v0.2#\n##################")
b = str(input("\nВыберите действие(*,/,+,-,**,//): "))
if b == "*":
    a = int(input("Введите первый множитель: "))
    d = int(input("Введите второй множитель: "))
    print("Ответ:", a * d, sep=" ")
elif b == "/":
    a = int(input("Введите делимое: "))
    d = int(input("Введите делитель: "))
    print("Ответ:", a / d, sep=" ")
elif b == "+":
    a = int(input("Введите первое слагаемое: "))
    d = int(input("Введите второе слагаемое: "))
    print("Ответ:", a + d, sep=" ")
elif b == "-":
    a = int(input("Введите уменьшаемое: "))
    d = int(input("Введите вычитаемое: "))
    print("Ответ:", a - d, sep=" ")
elif b == "**":
    a = int(input("Введите основание: "))
    d = int(input("Введите показатель: "))
    print("Ответ:", a ** d, sep=" ")
elif b == "//":
    a = int(input("Введите делимое: "))
    d = int(input("Введите делитель: "))
    print("Ответ:", a // d, sep=" ")
else:
    print("Ошибка")
input("Нажмите Enter для выхода")