class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()):
            return False
        
        pattern_dict = {}
        string_dict = {}
        for pattern, string in zip(pattern, s.split()):
            # print(pattern, string)
            if pattern not in pattern_dict and string not in string_dict:
                pattern_dict[pattern] = string
                string_dict[string] = pattern
            else:
                if pattern in pattern_dict:
                    if pattern_dict[pattern] != string:
                        return False
                if string in string_dict:
                    if string_dict[string] != pattern:
                        return False
        return True