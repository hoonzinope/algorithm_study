class Solution:
    def simplifyPath(self, path: str) -> str:
        while "//" in path:
            path = path.replace("//","/")
        if path[-1] == "/":
            path = path[:-1]
        folder_list = [folder for folder in path.split("/")]
        canonical = []
        for folder in folder_list:
            if folder == "..":
                if len(canonical) > 0:
                    canonical.pop()
            elif folder != ".":
                canonical.append(folder)
        canonical_folder = ""
        for i in range(len(canonical)):
            if canonical[i] == "":
                continue
            else:
                canonical_folder += "/"+canonical[i]
        
        if canonical_folder == "":
            canonical_folder = "/"
        
        return canonical_folder