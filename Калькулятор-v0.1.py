import math
print("##################\n#Калькулятор v0.1#\n##################")
b = str(input("\nВыберите действие(*,/,+,-,**): "))
a = float(input("Введите первое число: "))
d = float(input("Введите второе число: "))
if b == "*":
    c = a * d
    print("Ответ:", c, sep=" ")
elif b == "/":
    c = a / d
    print("Ответ:", c, sep=" ")
elif b == "+":
    c = a + d
    print("Ответ:", c, sep=" ")
elif b == "-":
    c = a - d
    print("Ответ:", c, sep=" ")
elif b == "**":
    c = a ** d
    print("Ответ:", c, sep=" ")
else:
    print("Ошибка")
input("Нажмите Enter для выхода")