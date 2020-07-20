class Solution:
    def longestCommonPrefix(self, strs):
        all_case = []
        
        for s_i in strs:
            jj = len(s_i)
            ii = 1
            while ii < jj+1:
                all_case.append(s_i[0:ii])    
                ii+=1
        
        str_dict={key: None for key in all_case}
        
        for k in str_dict: 
            str_dict[k] = all_case.count(k)
            
        if len(str_dict.values()) >0 :
            maxValue = max(str_dict.values()) 
            if maxValue >= len(strs):
                all_max = [key for key in str_dict.keys() if str_dict[key] == maxValue ]
                return(max(all_max, key=len))
            else:
                return("")
        else:
            return("")

if __name__ == '__main__' :
    out = Solution()
    print( out.longestCommonPrefix(["flower","flow","flight"]) )