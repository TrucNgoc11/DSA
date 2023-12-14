"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Link current node to dummy as head of the ans_list
        we have cur_sum = val node l1 + val node l2 + carry if yes
        Create a new node with the digit value of sum mod 10 and set it to cur node_next, then move forward cur node to next
        Time: O(m) or O(n) depends on which one is longer
        Space: O(1)
        """
        dummy = ListNode(0)
        cur_node = dummy
        carry_to_next = 0
        while l1 != None or l2 != None or carry_to_next != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_sum = l1_val + l2_val + carry_to_next
            carry_to_next = cur_sum // 10 #if cur_sum >= 10, have to bring carry to next cur_sum
            new_node = ListNode(cur_sum % 10)
            cur_node.next = new_node
            cur_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

        
