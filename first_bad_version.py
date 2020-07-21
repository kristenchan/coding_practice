class Solution:

    def isBadVersion(self, version):
        v = [False, False, False, True, True]
        return(v[version-1])

    def firstBadVersion(self, n):
        l, h = 1, n

        while l <= h:
            m = (l + h) // 2
            if self.isBadVersion(m):
                if m ==1 or not self.isBadVersion(m-1) :
                    return m
                h = m -1
            else:
                l = m +1
        return None

if __name__ == "__main__":
    out = Solution()
    print(out.firstBadVersion(5))



