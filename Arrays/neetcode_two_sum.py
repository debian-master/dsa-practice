# Problem Link:
# https://neetcode.io/problems/two-integer-sum?list=neetcode150

"""
Constraints
    - Assume Only one possible solution exists
    - Confirm the array is sorted or unsorted?
    - Is only one solution guaranteed?
    - What does it mean by `Return the answer with the smaller index first.`

Category
    - Hashing, Sorting, Two Pointers, Sliding Window?

"""


# Solution 1:
"""
Brute Force Solution
"""
class Solution1:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # brute force solution
        for num_i in range(len(nums)):
            for num_j in range(len(nums)):
                if num_i == num_j:
                    continue

                if (nums[num_i] + nums[num_j]) == target:
                    return [num_i, num_j]

print(Solution1().two_sum([1,2,3,4,5,6], 7))


# Solution 2
"""
This solution is workable but Dict will always store last element of repeated number,
Still uses two loops but more optimised than first solution.
"""
class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_len = len(nums)
        num_mapper = {
            nums[num_i]: num_i for num_i in range(num_len)
        }
        for num_i in range(num_len):
            remaining = target - nums[num_i]
            remaining_index = num_mapper.get(remaining)
            if (
                remaining_index is not None
                and remaining_index != num_i
            ):
                return [num_i, remaining_index]

print(Solution2().two_sum([1,2,3,4,5,6], 7))


# Solution 3
"""
Optimised solution for this problem, One Pass solution
"""
class Solution3:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_mapper = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in num_mapper:
                return [num_mapper[remaining], i]

            num_mapper[num] = i

print(Solution3().two_sum([1,2,3,4,5,6], 7))
