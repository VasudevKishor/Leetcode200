class Solution:
    def reverse(self, x: int) -> int:
        StringX = str(x)
        if x < 0:
            reversed_str = StringX[:0:-1]
            reversed_int = -int(reversed_str)
        else:
            reversed_str = StringX[::-1]
            reversed_int = int(reversed_str)
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
    
        return reversed_int
