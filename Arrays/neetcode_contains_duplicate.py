# Problem Link
# https://neetcode.io/problems/duplicate-integer?list=neetcode150

"""
Constraints
    - is the array sorted or unsorted?
    - Any limitation on modifying the input?
    - Speed vs Memory?
"""

# Solution 1:
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


# Solution 2:
"""
Much more cleaner version (Easy to understand)
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True

            nums_set.add(num)

        return False


# Solution 3:
"""
Pythonic way
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

print(Solution().hasDuplicate(nums=[1,2,3,3]))
