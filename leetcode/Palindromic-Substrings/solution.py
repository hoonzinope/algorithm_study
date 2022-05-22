class Solution:
    def isPain(self,string, visited):
        if len(string) % 2 == 1:
            if string[1:len(string)-1] not in visited:
                if self.isPain(string[1:len(string)-1], visited):
                    if string[0] == string[-1]:
                        visited[string] = True
                        return True
                    else:
                        visited[string] = False
                        return False
                else:
                    visited[string] = False
                    return False
            else:
                if visited[string[1:len(string)-1]]:
                    if string[0] == string[-1]:
                        visited[string] = True
                        return True
                    else:
                        visited[string] = False
                        return False
                else:
                    visited[string] = False
                    return False
        else:
            r_string = string[len(string)//2:][::-1]

            if string[:len(string)//2] == r_string:
                visited[string] = True
                return True
            else:
                visited[string] = False
                return False
    
    def countSubstrings(self, s: str) -> int:
        
        result_set = []
        visited = {}
        for i in range(1, len(s)+1):
            for j in range(len(s)-(i-1)):
                sub = s[j:j+i]
                if sub not in visited:
                    if self.isPain(sub, visited):
                        result_set.append(sub)
                    else:
                        continue
                else:
                    if visited[sub]:
                        result_set.append(sub)
        # print(result_set)
        return len(result_set)
        