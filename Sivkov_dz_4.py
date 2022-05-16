# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

#from sys import argv
#def zp (vir, stavka, prem):
#    return ((vir*stavka)+prem)

# далее вызов из терминала с тремя параметрами.

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
# формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

#spisok=(300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)

#def gen (a, b):
#    if int(b) > int(a):
#        return b
#    else:
#        return 0

#new_spisok = []

#for el in spisok:
#    result=int(gen(a, el))
#    if result > 0:
#        new_spisok.append(result)
#    a = el
#print(f"Исходный список: {spisok}")
#print(f"Новый список: {new_spisok}")

#  3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
# строку.
# Подсказка: используйте функцию range() и генератор.

#from random import randrange
#print([el for el in range(20, 240) if el % 21 == 0])
#print([el for el in range(20, 240) if el % 20 == 0])

# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
# порядке их следования в исходном списке. Для выполнения задания обязательно используйте
# генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

spisok=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
povtor=[]

for i in spisok:
    c = spisok.count(i)
    if c > 1:
        povtor.append(i)

print(f"Исходный список: {spisok}")
print(f"Список значений, которые повторяются: {povtor}")

for i in povtor:
    for j in spisok:
        if i == j:
            spisok.remove(j)

print(f"Результирующий список: {spisok}")


#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

#from random import randrange
#from functools import reduce

#spisok = ([el for el in range(100,1001) if el % 2 == 0])
#print(spisok)

#def umnog(a, b):
#    return a * b

#print(reduce(umnog, spisok))

#6. Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.
#Подсказка: используйте функцию count() и cycle() модуля itertools.
#Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при
# котором повторение элементов списка прекратится.


#from itertools import count, cycle

#spisok = []
#spisok2 = []

#a= int(input('Введите число с которого начнется список (1-10): '))

#for el in count(a):
#    if el > 13:
#        break
#    else:
#        print(el)
#        spisok.append(el)

#print(spisok)

#b = 0
#c = int(input('Введите число копий (рекоменд. не более 10): '))

#for el in cycle(spisok):
#    if b > c:
#        break
#    print(el)
#    spisok2.append(el)
#    b = b + 1

#print(spisok2)


#7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
#import math

#a = [1, 2, 3, 4, 5]
#def fact (a):
#    for el in (a):
#        yield math.factorial(el)

#g = fact(a)
#print(g)

#for el in fact(a):
#    print(el)
