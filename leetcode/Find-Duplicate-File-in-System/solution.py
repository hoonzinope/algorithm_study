class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        file_dict = {}
        for path in paths:
            infos = path.split(" ")

            directory = infos[0]
            for i in range(1, len(infos)):
                file_name = infos[i]

                content = file_name.split("(")[1].replace(")","")
                file_name = file_name.split("(")[0]

                # print(directory, file_name, content)

                if content in file_dict:
                    file_dict[content].append(directory+"/"+file_name)
                else:
                    file_dict[content] = [directory+"/"+file_name]
                
        result = [val for key, val in file_dict.items() if len(val) != 1]
        result = sorted(result, key=lambda x : len(x), reverse=True)
        
        return result
            