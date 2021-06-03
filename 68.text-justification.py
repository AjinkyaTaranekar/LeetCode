#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        string = []
        count = 0
        w = 0
        while w < len(words):
            word = words[w]
            curr_len = sum(len(w) for w in string) + count
                
            if len(word) + curr_len <= maxWidth:
                string.append(word)
                count += 1
                w += 1
            else:
                extra_spaces = maxWidth - curr_len + 1
                print(string)
                if len(string) == 1:
                    string = string[0] + ' ' * extra_spaces
                else:
                    while extra_spaces != 0:
                        for i in range(len(string)-1):
                            if extra_spaces:
                                string[i] = string[i] + ' '
                                extra_spaces -= 1
                            else:
                                break
                    string = ' '.join(string)
                res.append(string)
                string = []
                count = 0
        
        curr_len = sum(len(w) for w in string) + count
        extra_spaces = maxWidth - curr_len + 1
        string = ' '.join(string) + ' ' * extra_spaces
        res.append(string)
        return res
# @lc code=end

