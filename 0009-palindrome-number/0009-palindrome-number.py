class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        #flag=True
        for i in range(n//2+1):
            if x[i]!=x[n-i-1]:
                return False
        return True
        