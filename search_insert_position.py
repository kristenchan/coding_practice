class Solution:
    def searchInsert(self, nums, target):
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else :
                h = m-1
        return l


if __name__ == "__main__":
    out = Solution()
    print( '[2,3,5,6], 1' ,': ', out.searchInsert([2,3,5,6], 1) )
    print( '[1,3,5,6], 1' ,': ', out.searchInsert([2,3,5,6], 2) )
    print( '[2,3,5,6], 3' ,': ', out.searchInsert([2,3,5,6], 3) )
    print( '[2,3,5,6], 6' ,': ', out.searchInsert([2,3,5,6], 6) )
    print( '[2,3,5,6], 7' ,': ', out.searchInsert([2,3,5,6], 7) )