
number = float(input("Введите число "))
if number < 0:
    raise Exception("Число должно быть больше 0")
rub = int(number)
kop = int((number - int(number))* 100)
print(rub,'руб.', kop,'коп.')