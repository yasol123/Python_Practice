#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        maximum depth - # of nodes along the longest path from root -> leaf node
        Approach: Recursion
        n = number of nodes
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root: #if the root is null, return 0.
            return 0
        #recursive function calls and choose which one is bigger since the tree is not balanced
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1 
