
nums = [x for x in range(1, 11)]
print('numbers: ' + str(nums))

mid = len(nums)//2

print('first three items:  ' + str(nums[:3]))
print('middle three items: ' + str(nums[mid-1:mid+2]))
print('last three items:   ' + str(nums[-3:]))
