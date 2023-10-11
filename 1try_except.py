# правильное исполнение
string = "5"
number = int(string)
print(number)

# неверное исполнение
string = "hello"
number = int(string)
print(number)

# пользоательский ввод
string = input("Введите число: ")
number = int(string)
print(number)

# исключение всех типов
try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
# finally:
#     print("Блок try завершил выполнение")    
print("Завершение программы")

# исключение типа ValueError (например, неудачное преобразование строки в число)
try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError:
    print("Преобразование прошло неудачно")
print("Завершение программы")

# разные типы исключений
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение")
print("Завершение программы")

# ситуация не предусмотренности нужного исключения 
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
print("Завершение программы")

# множественные исключения 
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except (ZeroDivisionError, ValueError):    #  обработка двух типов исключений - ZeroDivisionError и ValueError
    print("Попытка деления числа на ноль или некорректный ввод")
print("Завершение программы")

# получение информации об исключении 
try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError as e:
    print("Сведения об исключении", e)
print("Завершение программы")

# самопальное исключение с помощью raise
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number2 == 0:
        raise Exception("Второе число не должно быть равно 0")
    print("Результат деления двух чисел:", number1/number2)
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
print("Завершение программы")