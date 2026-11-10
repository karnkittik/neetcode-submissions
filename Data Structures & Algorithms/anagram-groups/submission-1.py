class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            order_word = "".join(sorted(list(word)))
            if  order_word in anagram:
                anagram[order_word].append(word)
            else:
                anagram[order_word] = [word]
        return list(anagram.values())