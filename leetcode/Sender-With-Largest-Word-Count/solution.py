class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        name_dict = {}
        for m, s in zip(messages, senders):
            if s not in name_dict:
                name_dict[s] = len(m.split(" "))
            else:
                name_dict[s] += len(m.split(" "))
        
        return sorted(name_dict.items(), key=lambda x : (x[1],x[0]), reverse=True)[0][0]