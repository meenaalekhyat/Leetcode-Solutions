class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, high=0,0
        mappy=set()
        max_length=0
        while high<len(s):
            if s[high] not in mappy:
                mappy.add(s[high])
                high+=1
                max_length=max(max_length, high-low)
            else:
                mappy.remove(s[low])
                low+=1
        return max_length
