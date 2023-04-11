# for i  in range (1,6,2):
#   print(i)
# word = "Hello world"
# for i in word:
#     print(i)
# перебор строки цикл for
# count=0
# word = "Hello world"
# for i in word:
# if i =="l":
#   count+=1
#   print("count", count)
i = 5
while i <= 15:# Цикл
    print(i)
    i += 2

isHaCar =True
while isHaCar:
    if input("Enter data: ")== "Stop":
        isHaCar = False

for i in range(1,11):
    if i ==5:
        break # выход из цикла
        if i % 2==0:
            continue # пропуск итерации
    print(i)

found= None # Значение *Ничего*
for i in "hello":
    if i =="l":
        found = True
        break # оператор выхода из цикла
else:
    found = False

