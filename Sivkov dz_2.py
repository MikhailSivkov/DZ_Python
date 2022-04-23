#Задание 1
#some_list = ['hello', 123, True, '213 код']
#print(some_list[0])
#print(type(some_list[0]))
#print(some_list[1])
#print(type(some_list[1]))
#print(some_list[2])
#print(type(some_list[2]))
#print(some_list[3])
#print(type(some_list[3]))
#print([type (i) for i in some_list]) #вариант 2

#Задание 2
#i = 1
#v_list =[]
#s_list =[]
#p = int(input('Вам необходимо ввести список цифр, скажите сколько цифр вы будете вводить? '))
#while i <= p:
#    number = input('введите числo: ')
#    s_list.append(number)
#    i += 1
#i = 0
#if p%2 == 0:
#    while i <= (p - 1):
#        a = s_list[i + 1]
#        b = s_list[i]
#        v_list.append(a)
#        v_list.append(b)
#        i += 2
#else:
#    p = p-1
#    while i <= (p - 1):
#        a = s_list[i + 1]
#        b = s_list[i]
#        v_list.append(a)
#        v_list.append(b)
#        i += 2
#    v_list.append(s_list[-1])
#print(v_list)

#Задание 3
#number_month=int(input('введите номер месяца: '))
#month = {1 : 'зима', 2 : 'зима', 12 : 'зима', 3 : 'весна', 4 : 'весна', 5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето', 9 : 'осень', 10 : 'осень', 11 : 'осень',}
#print(month.get(number_month))

#Задание 4
#some_list=input('введите слова через пробел: ')
#s_list=some_list.split(' ')
#print(s_list)
#i = 0
#while i < len(s_list):
#    el = s_list[i]
#    if len(el) > 10:
#        print(el[0:10])
#    else:
#        print(el)
#    i += 1

#Задание 5
#my_list=[7, 5, 3, 3, 2]
#el = int(input('Введите число: '))
#my_list.append(el)
#my_list.sort()
#my_list=my_list[::-1]
#print(my_list)

#Задание 6
korteg=[
    (1, {'название':'компьютер', 'цена':20000, 'количество':5, 'ед':'шт.'}),
    (2, {'название':'принтер', 'цена':6000, 'количество':2, 'ед':'шт.'}),
    (3, {'название':'сканер', 'цена':2000, 'количество':7, 'ед':'шт.'})
]
d_1=dict(korteg[0][1])
d_2=dict(korteg[1][1])
d_3=dict(korteg[2][1])

list_name = [d_1.get('название'), d_2.get('название'), d_3.get('название')]
list_prise = [d_1.get('цена'), d_2.get('цена'), d_3.get('цена')]
list_vol = [d_1.get('количество'), d_2.get('количество'), d_3.get('количество')]
list_ed = [d_1.get('ед')]

result = list(d_1.keys())
dict_res = {result[0]:list_name, result[1]:list_prise, result[2]:list_vol, result[3]:list_ed}
print(dict_res)
