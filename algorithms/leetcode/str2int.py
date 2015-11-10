class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        str = str.strip()
        if str[0] not in ["0","1","2","3","4","5","6","7","8","8","0","-","+"]:
            return 0
        elif str[0] == "-":
            sign = -1
            limit = 2147483648
            str = str[1:]
        elif str[0] == "+":
            sign = 1
            limit = 2147483647
            str = str[1:]
        else:
            sign = 1
            limit = 2147483647
        nums = str
        i = 0
        current = 0
        dot = 0
        while i < len(nums) and dot < 1:
            if nums[i] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                break
            elif nums[i] == ".":
                dot += 1
            if dot == 0:
                if current <= 1.0 * (limit - int(nums[i])) / 10:
                    current = current * 10 + int(nums[i])
                else:
                    return sign * limit
            else:
                current = current + 0
            i += 1
        return sign * current
