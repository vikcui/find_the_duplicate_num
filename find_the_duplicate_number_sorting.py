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
    :time complexity: O(nlogn)
    :space complexity: O(1)
    """
    # first sort the list O(nlogn)
    nums.sort()
    # one pass thru the list to find the duplicate O(n)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]


# print(findDuplicate([1,3,4,2,2]))