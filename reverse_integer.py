class Solution:
    def reverse(self, x: int) -> int:  
        if x > 0:  # handle positive numbers  
            z =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            z = -1 * int(str(x*-1)[::-1])  
        if z not in range((-2**31), (2**31 - 1)):  
            return 0  
        else:  
            return z

""" 
#---------- Version 1 --------
class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if x < 0:
            y = y[1:]
        z = 0
        l = len(y)
        for i in range(0, l):
            z += int(y[l-i-1])*(10**(l-i-1))    
            
        if (x < 0 and 0-z > -0x80000000) :
        	return(0-z)
        elif (x > 0 and z < 0x7fffffff):
        	return(z)
        else:
        	return(0)
"""

if __name__ == '__main__' :
    out = Solution()
    print( out.reverse(123) )
