#nums = [1,2,3]
#nums.append(4)
#print(nums)


words = ["Python", "fun"]
words.insert(1,"is")
print(words)



#nums=[9,8,7,6,5]
#nums.append(4)
#nums.insert(2,11)
#print(len(nums))


#letters = ["p","q","r","s","p","u"]
#print(letters.index("r"))
#print(letters.index("p"))
#print(letters.index("q"))


#x = [2,4,5,7,4]
#y = x.index(4)
#print(y)


x = [2,4,6,2,7,2,9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)



list = [8,4,2,6]
list.remove(2)
print(len(list)+list.count(6))


queue = ["john", "Amy","Bob","Adam"]
name =input()
queue.append(name)
print(queue)


nums = [2,4,8,9,5]
nums.insert(1,3)
nums.remove(9)
nums.insert(0, nums.count(8))
print(nums[3])