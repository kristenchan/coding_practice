class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        i = head
        while i :
            tmp = i.next
            while tmp and tmp.val == i.val:
                # tmp is not None and tmp.val == i.val
                tmp = tmp.next
            i.next = tmp
            i = i.next
        return i




