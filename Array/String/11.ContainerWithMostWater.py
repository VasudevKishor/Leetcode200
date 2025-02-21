class Solution(object):
    def maxArea(self, height):
        max_area = 0            #initialze max_area as zero. So that we can incr that with each iteration
        left = 0               #initialize left pointer as 0. Start from the left
        right = len(height) - 1 #initialize right pointer as len(height) - 1. Start from the right
        while left < right:  
            max_area = max(max_area, min(height[left], height[right]) * (right - left)) #calculate the area and update max_area
            #The area of the container depends on the length of the containers (right-left).
            #area of the container depends on the smaller height of the side 
                    #therefore, min(height[left],height[right]) is used.
                    #By this, we can calculate woth respect to the smaller side.
            #The area of the container is given by 
                # [height * length]
                # here, in code, we represent it by min(height[left],height[right])*(right-left)
            if height[left] < height[right]:
                left += 1 #increments to the next index for further calculation
            else:
                right -= 1 #decrements to the next index for further calculation
        return max_area