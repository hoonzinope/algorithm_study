class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        for x, y in zip(v1, v2):
            v1_num = int(x)
            v2_num = int(y)
            if v1_num > v2_num:
                return 1
            elif v1_num < v2_num:
                return -1
        
        if len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                if int(v1[i]) != 0:
                    return 1
        elif len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                if int(v2[i]) != 0:
                    return -1
        return 0
        