class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def wordvectorReturn(word):
            vector = [0] * 26
            for w in word:
                vector[ord(w)-ord('a')] += 1
            return vector
        
        words2_vec = [0] * 26
        for word in words2:
            vector = wordvectorReturn(word)
            for i in range(len(vector)):
                words2_vec[i] = max(words2_vec[i], vector[i])
        answer = []
        for word in words1:
            vector = wordvectorReturn(word)
            
            flag = True
            for i in range(len(vector)):
                if words2_vec[i] > vector[i]:
                    flag = False
                    break
            if flag:
                answer.append(word)
        return answer