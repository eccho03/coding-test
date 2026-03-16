class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height)-1
        answer=0

        while start<end:
            h = min(height[start], height[end])
            w = end-start
            answer = max(answer, h*w)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return answer

        