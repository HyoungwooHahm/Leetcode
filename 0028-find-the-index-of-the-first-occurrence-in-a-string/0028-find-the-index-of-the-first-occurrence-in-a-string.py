class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            haystack=haystack.replace(needle,"1")
            return haystack.index("1")