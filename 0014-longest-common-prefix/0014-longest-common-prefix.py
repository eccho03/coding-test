class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        target=strs[0]

        for i in range(1,len(strs)):
            cur = strs[i]
            tmp = ""

            for j in range(min(len(target),len(cur))):
                if target[j]==cur[j]:
                    tmp+=cur[j]
                else:
                    break
            target=tmp
            
        return target