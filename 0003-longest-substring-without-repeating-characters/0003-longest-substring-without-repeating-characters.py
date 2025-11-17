class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        mx_len = 0
        tmp=set()

        for right in range(len(s)):
            while s[right] in tmp:
                tmp.remove(s[left])
                left+=1
            tmp.add(s[right])
            mx_len = max(mx_len, right-left+1)
            
        return mx_len