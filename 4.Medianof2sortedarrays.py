class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        final = nums1 + nums2
    
        final.sort()
        if len(final)%2==0:
            return (final[int(len(final)/2-1)]+final[int(len(final)/2)])/2.0
        else:
            return final[int(len(final)/2)]

v = Solution()
print(v.findMedianSortedArrays([1,3],[2]))