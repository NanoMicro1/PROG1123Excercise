# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l1 = [2,4,3]
#         l2 = [5,6,4]

#         l1.head_node = ListNode(2)
#         l1.head_node.next = Listnode(4)
#         l1.head_node.next.next = Listnode(3)

#         l2.head_node = ListNode(5)
#         l2.head_node.next = ListNode(6)
#         l2.head_node.next.next = ListNode(4)

#     #sum = 

# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # l1, l2 인스턴스 초기화 부분 삭제 또는 주석 처리

#         l1 = ListNode(2)
#         l1.next = ListNode(4)
#         l1.next.next = ListNode(3)

#         l2 = ListNode(5)
#         l2.next = ListNode(6)
#         l2.next.next = ListNode(4)

#         # ... 나머지 로직

from typing import List

class LIST:
    def __init__(self, val, next=None):
        self.val = val
        # self.val2 = val2
        # self.val3 = val3
        # self.next = next 
    
class Contents:
    def numbers(self, l1: List[LIST]) -> None:

        l1 = [LIST(2), LIST(4)]
        for node in l1:
            print(node.val)
        
contents = Contents()
contents.numbers([])