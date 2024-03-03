#!python3
nums = [1, 2, 5, 8]

print('natural list {nums}')

nums.append(3)
nums.append(7)
nums.append(6)

print(len(nums))
nums[3] = 200

nums.insert(0, 100)

print(f'apendado {nums}')