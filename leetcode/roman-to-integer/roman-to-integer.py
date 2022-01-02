class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_number = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        except_number = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        
        result = 0
        for roman, value in except_number.items():
            while roman in s:
                result += except_number[roman]
                s = s.replace(roman, '')
        
        if len(s) != 0:
            for roman in s:
                result += roman_number[roman]
                
        
        return result