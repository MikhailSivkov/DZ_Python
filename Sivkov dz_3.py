#Задание 1
#a1 = int(input('Введите первое число: '))
#a2 = int(input('Введите второе число: '))
#if a2 != 0:
#    result= a1/a2
#    print('Результат деления: ', round(result,3))
#else:
#    print('Делить на ноль нельзя')

#Задание 2
#name = input('Введите свое имя: ')
#sname = input('Введите свою фамилию: ')
#y_b = input('Введите год рождения: ')
#city = input('Введите город проживания: ')
#email = input('Введите свой e-mail: ')
#n_phone = input('Введите свой номер телефона: ')

#def name_id(name, sname, y_b, city, email, n_phone):
#    result = name+' '+sname+' '+y_b+' '+city+' '+email+' '+n_phone
#    return result
#print(name_id(name, sname, y_b, city, email, n_phone))

#Задание 3
#def maximum(x,y,z):
#    list1 = [x, y, z]
#    print(list1)
#    list1.sort()
#    print(list1)
#    list_res=list1[-2:]
#    print(list_res)
#    return list_res
#print(maximum(5,8,1))

#Задание 4 вариант 1
#def my_func(x, y):
#    result=x**y
#    return result
#print(my_func(2, -1))

#Задание 4 вариант 2 не сделал
#def my_func(x, y):
#    i=1
#    res=x
#    while i <= abs(y):
#        res=res*х
#        i+=1
#        print(res)
#    return res
#print(my_func(2, -1))

#Задание 5
#sum=0

#def summ(numbers):
#    b = [int(item) for item in numbers.split()]
#    num=list(map(int, b))
#    global sum
#    i=0
#    while i < len(num):
#        sum=sum+num[i]
#        i+=1
#        print(sum)
#    return sum

#numbers = input('Введите целые числа через пробел: ')
#print('Сумма элементов: ', summ(numbers))
#numbers = input('Если хотите еще ввести цифры для сложения, то введите целые числа через пробел: ')
#print('Сумма элементов: ', summ(numbers))

#Задача 6
def int_func(str):
    return(str.title())
print(int_func('text'))

#Задача 7
fraza=input('Введите слова через пробел: ')
c = [int_func(item) for item in fraza.split()]
print(' '.join(c))
i=0
while i < len(c):
    print(c[i])
    i+=1
