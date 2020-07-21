class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        d_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in d_nums:
                return [d_nums[target - nums[i]], i]
            else :
                d_nums[nums[i]] = i
        return(result)

""" 
#---------- Version 2 --------
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        d_nums = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            if target - nums[i] in d_nums:
                if i == d_nums[target - nums[i]]:
                    continue
                else :
                    result = [i, d_nums[target - nums[i]]]
                break
        return(result)
"""

""" 
#---------- Version 1 --------
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        r_l = list(set(nums).intersection(set([x - y for x, y in zip([target]*len(nums), nums)])))
        
        if len(r_l) >2: 
            if target % 2 == 0:
                r_l.remove(target/2)  
            o=[nums.index( r_l[0]),nums.index( r_l[1])]
        elif len(r_l) == 2:
            o=[nums.index( r_l[0]),nums.index( r_l[1])]
        elif len(r_l) == 1:
            o=[i for i,n in enumerate(nums) if n == r_l[0]]
            
        return(o)
 """

if __name__ == '__main__' :
    out = Solution()
    #print( out.twoSum([2, 7, 11, 15], 9) )
    print( out.twoSum([3, 2, 4], 6) )