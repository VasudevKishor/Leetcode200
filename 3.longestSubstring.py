class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxL = 0  # Stores the maximum length of a unique substring
        
        for i in range(len(s)):
            elem = set()  # Using a set instead of a list for faster lookups
            localMax = 0  # Tracks the length of the current unique substring
            
            for j in range(i, len(s)):  # Expanding the substring from index i
                if s[j] in elem:
                    break  # Stop when we find a duplicate
                elem.add(s[j])  # Add the new character to the set
                localMax += 1  # Increase the length of the current substring
            
            maxL = max(maxL, localMax)  # Update maxL if a longer substring is found
        
        return maxL
