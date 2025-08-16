# Problem Link
# https://neetcode.io/problems/duplicate-integer?list=neetcode150

""" Constraints
    - is the array sorted or unsorted?
    - Any limitation on modifying the input?
    - Speed vs Memory?
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_set: set[int] = set()
        for num in nums:
            number_exists = num in nums_set
            if not number_exists:
                nums_set.add(num)
                continue

            return True

        return False

print(Solution().hasDuplicate(nums=[1,2,3,3]))
