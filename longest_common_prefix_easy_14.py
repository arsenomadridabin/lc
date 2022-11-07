class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        smallest = ""
        length = inf
        for str_val in strs:
            l = len(str_val)
            if l < length:
                length = l

        for i in range(length):
            unique = []
            for str_val in strs:
                unique.append(str_val[i])
            unique_list = list(set(unique))
            if len(unique_list) == 1:
                smallest = smallest + unique_list[0]
            else:
                break
        return smallest
                