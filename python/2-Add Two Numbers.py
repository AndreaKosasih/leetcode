# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(out)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Helper function to create linked list from list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(node):
    nodes = []
    while node:
        nodes.append(str(node.val))
        node = node.next
    print(" -> ".join(nodes))

# Example usage
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1