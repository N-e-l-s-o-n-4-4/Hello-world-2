if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

# county = "US"
# age = 42
# if (county == "US" or county == "GB") and (age > 0 and < 100):
# print("cool")
age = int(input())
if 0 <= age <= 11:
    print("Child")
elif 12 <= age <= 17:
    print("Teen")
elif 18 <= age <= 64:
    print("Adult")
