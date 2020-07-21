class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t : return True
        if len(s) == len(t):
            sTot = len(set(s))
            for i in set(s):
                if s.count(i) != t.count(i): return False
                if s.count(i) == t.count(i):
                    sTot -= 1
                    if sTot == 0:
                        return True

'''
#---------- Version 1 --------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        if s == t :
            result = True
        elif len(s) == len(t):
            #sMap = dict.fromkeys(set(s), 0)
            sTot = len(set(s))
            for i in set(s):
                if s.count(i) != t.count(i):
                    break
                else :
                    sTot -= 1
                    if sTot == 0:
                        result = True
        return(result)
'''

if __name__ == '__main__' :
    out = Solution()
    print( out.isAnagram("anagram", "nagaram") )
    print( out.isAnagram("rat", "car") )
    print( out.isAnagram("", "") )