# author: YANG CUI
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n
(inclusive), prove that at least one duplicate number must exist. Assume that there is
only one duplicate number, find the duplicate one.

Set in both Python and Java rely on underlying hash tables, so insertion and lookup
have amortized constant time complexities. The algorithm is therefore linear,
as it consists of a for loop that performs constant work n times.
"""

def findDuplicate(nums):
    """
    :param nums: input list where the duplicate is at
    :return: the duplicate
    :time complexity: O(n)
    :space complexity : O(n)
    """
    numSet = set()
    for num in nums:
        if num in numSet:
            return num
        numSet.add(num)

# print(findDuplicate([3,1,3,4,2]))