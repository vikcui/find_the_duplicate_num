# author: YANG CUI
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n
(inclusive), prove that at least one duplicate number must exist. Assume that there is
only one duplicate number, find the duplicate one.
"""

def findDuplicate(nums):
    """
    :param nums: input list where the duplicate is at
    :return: the duplicate
    :time complexity: O(n)
    :space complexity : o(1)
    not fast practically tho
    """
    # Find the intersection point of the two runners.
    tortoisePointer = nums[0]
    harePointer = nums[0]
    keepLooping = True
    while keepLooping:
        tortoisePointer = nums[tortoisePointer]
        harePointer = nums[nums[harePointer]]
        if tortoisePointer == harePointer:
            keepLooping = False
    # find the duplicate
    pointer1 = nums[0]
    pointer2 = tortoisePointer
    while pointer1 != pointer2:
        pointer1 = nums[pointer1]
        pointer2 = nums[pointer2]

    return pointer2


print(findDuplicate([2,5,9,6,9,3,8,9,7,1]))


