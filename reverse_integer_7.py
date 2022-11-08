class Solution:
    def reverse(self, x: int) -> int:
        val = str(x)
        if x < 0:
            val = str(-1 * x)
        reverse_val = int(val[::-1])
        import math
        if reverse_val > math.pow(2,31) -1 or reverse_val < -1 * math.pow(2,31):
            return 0
        else:
            if x<0:
                return -1*reverse_val
            else:
                return reverse_val
        
        