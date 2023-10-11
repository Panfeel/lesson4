# ОТКРЫТИЕ ФАЙЛА

# в лоб
myfile = open("text.txt", "w")
myfile.close()

# подстраховываемся исключениями
try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

# ЗАПИСЬ В ФАЙЛ

# правильная коснтрукция 
with open("hello.txt", "w") as somefile:
    somefile.write("hello world")    

# дозапись
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")  # пару слов про управляющие символы

# Дозапись через print()
with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)    


# ЧТНЕНИЕ ФАЙЛА

# построчное считывание
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

# построчное считывание (явное)
with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

# построчное считывание через while readline()
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

# разованое считывание небольшого файла read()
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# считывание небольшого файла в список readlines()
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)    