class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        new_title = ""
        for token in title.split():
            if len(token) <= 2:
                token = "".join([t.lower() for t in token])
            else:
                token = token[0].upper()+"".join([t.lower() for t in token[1:]])
            new_title+=token+" "
            
        return new_title.strip()