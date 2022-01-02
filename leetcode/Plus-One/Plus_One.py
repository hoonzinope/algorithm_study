class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        addNum = 1
        for index in range(len(digits)-1, -1, -1):
            digit = digits[index]
            digit = digit + addNum
            if digit >= 10:
                digits[index] = digit%10
                addNum = digit//10
            else:
                digits[index] = digit
                addNum = 0
        if addNum != 0:
            digits.insert(0,addNum)
        return digits