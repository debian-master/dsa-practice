# Problem Link:
# https://neetcode.io/problems/is-anagram?list=neetcode150

"""
Constraints
    - What characters are allowed?
    - Should the comparison be case-insensitive or ignore whitespace/punctuation?
"""


# Solution 1:
"""
More simpler and easy to understand solution
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s != len(t):
            return False

        s_hash = {}
        t_hash = {}
        for i in range(0, len_s):
            s_hash[s[i]] = (s_hash.get(s[i]) or 0) + 1
            t_hash[t[i]] = (t_hash.get(t[i]) or 0) + 1

        word_set = set(s)
        for word in word_set:
            if s_hash.get(word) != t_hash.get(word):
                return False

        return True


# Solution 2:
"""
More optimised solution where don't need to maintain two dictionaries
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s != len(t):
            return False

        counts = {}
        for i in range(0, len_s):
            counts[s[i]] = (counts.get(s[i]) or 0) + 1
            counts[t[i]] = (counts.get(t[i]) or 0) - 1

        for count in count.values():
            if count != 0:
                return False

        return True
