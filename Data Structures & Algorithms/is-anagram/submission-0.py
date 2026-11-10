class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_char_s = {}
        for i in s:
            if i in count_char_s:
                count_char_s[i] += 1
            else:
                count_char_s[i] = 1
        count_char_t = {}
        for i in t:
            if i in count_char_t:
                count_char_t[i] += 1
            else:
                count_char_t[i] = 1
        return count_char_s == count_char_t