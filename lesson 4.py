# temp = int(input())
# if temp >= int(100):
#    print("Boiling")
user_data = int(input("Введите  число: "))

isHappy = True

if isHappy and user_data == 6:
    print("User is happy")

if isHappy or user_data == 6:
    print("User is happy2")

elif user_data == 5:
    print("Number is 5")

elif user_data == 7:
    print("Number is 7")

else:
    print("User is unhappy")
# Тернарный оператор
data = input()
number = 5 if data == "Five" else 0

# if user_data != 5:
#   print("Мы на месте")
#    if user_data > 6:
#        print("Number is bigger than 5")
