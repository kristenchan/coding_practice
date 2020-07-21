class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,  'C': 100, 'D': 500, 'M': 1000}
        num_s = list(map(lambda x: roman[x], list(s)))
        return(sum([-num_s[i] if num_s[i+1] > num_s[i] else num_s[i] for i in range(0, len(num_s) - 1)]) + num_s[-1])

""" 
#---------- Version 1 --------
class Solution:
    def romanToInt(self, s: str) -> int:
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900} 
        normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        num = int()
        len_s = len(s)
        for k,v in special.items():
            s = s.replace(k, '')
            if len_s != len(s):
                num += v
                len_s = len(s)
        
        for k,v in normal.items():
            num += s.count(k)*v
        
        return(num)
"""

if __name__ == '__main__' :
    out = Solution()
    print( out.romanToInt('III') )