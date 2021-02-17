def removeDupes(nums):
    y = 0
    for x in range(len(nums)):
        if(nums[x] != nums[y]):
            y += 1
            nums[y] = nums[x]
    return y + 1


nums = [1, 1, 2]
print(removeDupes(nums=nums))
