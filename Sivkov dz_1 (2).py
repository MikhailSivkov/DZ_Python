# Задание 2
sek = int(input('Введите число секунд: '))
minut = sek // 60
chas = minut // 60
minut = minut % 60
sekund = sek % 60
print(chas, ':', minut, ':' , sekund)
