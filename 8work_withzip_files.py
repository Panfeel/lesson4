# создание и закрытие файла
from zipfile import ZipFile
myzip = ZipFile("arhiv.zip", "w")
myzip.close()

with ZipFile("metanit.zip", "w") as myzip:
    pass

# запись файлов в архив
with ZipFile("arhiv.zip", "a") as myzip:
    myzip.write("hello.txt")

# запись файлов в архив со сжатием
from zipfile import ZipFile, ZIP_DEFLATED
with ZipFile("arhiv.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
    myzip.write("hello.txt")


# получение информации о файлах в архиве   
with ZipFile("arhiv.zip", "a") as myzip:
    print(myzip.infolist())

with ZipFile("arhiv.zip", "r") as myzip:
    for item in myzip.namelist():
        print(item)    

# извлечение файлов из архива
with ZipFile("arhiv.zip", "r") as myzip:
    myzip.extractall() 

# считывание файла
with ZipFile("arhiv.zip", "r") as myzip:
    content = myzip.read("hello5.txt")
    print(content)


# открытие файла без извлечения
with ZipFile("arhiv.zip", "a") as myzip:
    # записываем в архив новый файл "hello5.txt"
    with myzip.open("hello5.txt", "w") as hello_file:
        encoded_str = bytes("Python...", "UTF-8")
        hello_file.write(encoded_str)
