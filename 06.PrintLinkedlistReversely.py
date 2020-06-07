# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 1. append to left
        # if head == None:
        #     return []
        # result = []
        # while head:
        #     result.insert(0, head.val)
        #     head = head.next
        # return result

        # 2. stack
        # if head == None:
        #     return []
        
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next

        # result = []
        # while stack:
        #     result.append(stack.pop())
        # return result    

        # 3.. reverse  the linkedlist
        # if head == None:
        #     return []
        
        # prev = None
        # next = None
        # cur = head

        # while cur:
        #     next = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next

        # result = []
        # while prev:
        #     result.append(prev.val)
        #     prev = prev.next
        # return result

        # 4. recursion
        if head == None:
            return []
        result = []
        self.printVal(result, head)
        return result
    
    def printVal(self, result, head):
        if head == None:
            return
        
        self.printVal(result, head.next)
        result.append(head.val)
