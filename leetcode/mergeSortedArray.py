# nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [1, 2, 2]
nums2 = [2, 5, 6]

nums2Index = 0

for x in range(len(nums1)):
    if nums1[x] == 0:
        if nums2Index > len(nums2)-1:
            nums1 = nums1.sort()
            # break
        else:
            nums1[x] = nums2[nums2Index]
            nums2Index += 1
# nums1 = sorted(nums1)
print(nums1)
