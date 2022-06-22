class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word]=1
            else:
                word_dict[word]+=1
        result = [(key,value) for key,value in word_dict.items()]
        result = sorted(result, key = lambda x : (-x[1], x[0].lower()))
        result = [ word[0] for word in result]
        return result[:k]