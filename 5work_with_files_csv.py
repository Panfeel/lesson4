import csv
 
# Запись в файл
#_____________________________________________________________________
FILENAME = "users.csv"
 
users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]
 
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
     
 
with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)


# Чтение из файла
#_____________________________________________________________________
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])    

# работа со словарем 
#_____________________________________________________________________
FILENAME = "users.csv"
 
users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]
 
with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
     
    # запись нескольких строк
    writer.writerows(users)
     
    user = {"name" : "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)
 
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])