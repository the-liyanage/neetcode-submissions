class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s , hashmap_t = {}, {}

        for character in s:
            if character not in hashmap_s:
                hashmap_s[character] = 1
            hashmap_s[character] += 1

        for character in t:
            if character not in hashmap_t:
                hashmap_t[character] = 1
            hashmap_t[character] +=1
        

        if hashmap_s == hashmap_t:
            return True
        return False
        