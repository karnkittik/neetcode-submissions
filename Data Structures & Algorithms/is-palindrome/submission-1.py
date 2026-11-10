class Solution:
    def isPalindrome(self, s: str) -> bool:
        character_only = [n.lower() for n in list(s) if n in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + list("abcdefghijklmnopqrstuvwxyz")+list("0123456789")]
        mid = len(character_only)//2
        if len(character_only)//2 == 0:
            return character_only[:mid] == character_only[:-mid:-1]
        else:
            return character_only[:mid] == character_only[:-mid-1:-1]