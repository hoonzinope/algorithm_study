class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations = sorted(equations, key=lambda x : ("==" in x), reverse=True)
        
        temp_dict = {}
        for equation in equations:
            val_a = equation[0]
            val_b = equation[-1]
            if equation[1:-1] == "==":
                if val_a not in temp_dict:
                    temp_dict[val_a] = set()
                    temp_dict[val_a].add(val_a)
                    temp_dict[val_a].add(val_b)
                else:
                    temp_dict[val_a].add(val_b)
                if val_b not in temp_dict:
                    temp_dict[val_b] = set()
                    temp_dict[val_b].add(val_a)
                    temp_dict[val_b].add(val_b)
                else:
                    temp_dict[val_b].add(val_a)
                    
                
                temp_dict[val_a].update(temp_dict[val_b])
                temp_dict[val_b].update(temp_dict[val_a])
                
                for a in temp_dict:
                    a_list = list(temp_dict[a])
                    for val in a_list:
                        temp_dict[val].update(temp_dict[a])
                        temp_dict[a].update(temp_dict[val])
            else:
                if (val_a in temp_dict and val_b in temp_dict[val_a]) or \
                (val_b in temp_dict and val_a in temp_dict[val_b]) or val_a == val_b:
                    return False
        return True