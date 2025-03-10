# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=dummyNode=ListNode()
        curr=dummyNode
        carry=0
        curr1=l1
        curr2=l2
        while (curr1!=None or curr2!= None):
            sums=carry
            if curr1:
                sums +=curr1.val
                curr1=curr1.next
            if curr2:
                sums +=curr2.val
                curr2=curr2.next
            newNode=ListNode(sums%10)
            carry=sums//10
            curr.next=newNode
            curr=curr.next
        if carry:
            newNode=ListNode(carry)
            curr.next=newNode
        return dummyNode.next
