
nums = []
rows = eval(input("请输入行数："))
columns = eval(input("请输入列数："))
index = 0
num = 0
for row in range(rows):
    nums.append([])
    for column in range(columns):
        # num = eval(input("请输入数字："))
        num +=1
        nums[row].append(num)

nums[0].append(0)
nums[0].append(0)
nums[0].append(0)

nums[1].append(1)
nums[1].append(1)

nums[2].append(2)
print(nums)

nums[0].clear()
print(nums)

nums.remove(nums[1])
print(nums)