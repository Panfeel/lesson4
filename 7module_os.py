import os

#создание папки
# путь относительно текущего скрипта
os.mkdir("hello")
# абсолютный путь
os.mkdir("C:/Users/panfi/YandexDisk/Для двух компов/СамГТУ/Курсы 2023/ТиМП/test_app/test")


#удаление папки
# путь относительно текущего скрипта
os.rmdir("hello")
# абсолютный путь
os.rmdir("C:/Users/panfi/YandexDisk/Для двух компов/СамГТУ/Курсы 2023/ТиМП/test_app/test")


# Переименование файла
os.rename("user.dat", "luser.dat")

# удаление файла
os.remove("luser.dat")

# существование файла
filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует") 
else:
    print("Файл не существует") 


