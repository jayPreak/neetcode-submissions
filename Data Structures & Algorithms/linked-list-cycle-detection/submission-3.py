# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        current1 = head
        current2 = head.next

        if current2 is None:
            return False

        print(current1.val)
        print('now inside')
        
        while current1 is not None or current2 is not None:
            # current2 = current1.next
            print(current1.val)
            
            if current1 == current2:
                return True
            print('meow')
            
            
            current1 = current1.next
            print("current1", current1.val)
            if current2 is None:
                return False
            print("current2", current2.val)
            move = current2.next
            if move is None:
                return False
            current2 = move.next

        return False
            
        