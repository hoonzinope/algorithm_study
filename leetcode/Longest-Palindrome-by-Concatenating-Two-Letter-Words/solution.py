class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        # print(word_dict)
        answer = 0
        same_word_flag = False
        check_word_set = set()
        for word in word_dict.keys():
            if word[::-1] in word_dict and word[::-1] not in check_word_set:
                if word[0] == word[1]:
                    if word_dict[word] % 2 == 1:
                        if same_word_flag == False:
                            same_word_flag = True
                            # print(word, 2*(word_dict[word]))
                            answer += 2*word_dict[word]
                        else:
                            answer += 2*(word_dict[word] - 1)
                    elif word_dict[word] % 2 == 0:
                        answer += word_dict[word]*2
                else:
                    small = word_dict[word] if word_dict[word] < word_dict[word[::-1]] else word_dict[word[::-1]]
                    # print(word_dict[word], word_dict[word[::-1]], small)
                    answer += 4*small
            check_word_set.add(word)
            check_word_set.add(word[::-1])
        return answer