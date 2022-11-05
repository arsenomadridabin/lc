class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        l_index = 0
        r_index = length-1
        l = numbers[l_index]
        r = numbers[r_index]
        while 1:
            if (l+r) > target:
                r_index = r_index -1 
                r = numbers[r_index]
            elif (l + r) < target:
                l_index = l_index + 1
                l = numbers[l_index]
            else:
                return [l_index+1,r_index+1]
            