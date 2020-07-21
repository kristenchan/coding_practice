class Solution:
    def isPalindrome(self, x):
        if x < 0:
            result =False 
        else:
            i = 0
            num = []
            while int(x) !=0:
                num.append(int(x % 10 ))
                x /= 10
                i += 1

            if i % 2 == 0:
                k1 = 0
                k2 = 1
            else : 
                k1 = 1
                k2 = 0

            m = int((i-k1)/2)
            result = True

            for j in range(1,m+1) :
                if num[m-j] == num[m+j-k2]:
                    continue
                else:
                    result =False
                break  
        
        return result

if __name__ == '__main__' :
    out = Solution()
    print( out.isPalindrome(121) )