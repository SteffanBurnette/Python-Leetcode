"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, 
except the number 0 itself./////l
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = []
        ll2 = []

        while l1:
            ll1.append(l1.val)
            l1 = l1.next #Moves to the next node
        while l2:
            ll2.append(l2.val)
            l2 = l2.next #moves to the next node
        
        print(ll1)
        print(ll2)
        # Convert integers to string, join, and convert back to integer
        if ll1:  # Only proceed if ll1 is not empty
            l1_num = int("".join(map(str, reversed(ll1))))
        else:
            l1_num = 0  # Or handle the empty case differently
        
        if ll2:  # Only proceed if ll1 is not empty
            l2_num = int("".join(map(str, reversed(ll2))))
        else:
            l2_num = 0  # Or handle the empty case differently

        # Convert number to list of integers
        n = l1_num + l2_num
        print(n)
        res = list(map(int, reversed(str(n))))

        #Instantiates the linkedlist that will be returned
        print(res)
        

        dummy = ListNode()  # Dummy node (does not hold actual data)
        current = dummy  # Pointer to build the list

        for x in res:
            current.next = ListNode(x)  # Create and link a new node
            current = current.next  # Move forw

        return dummy.next
