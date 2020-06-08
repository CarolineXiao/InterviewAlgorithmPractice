# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildSubTree(preorder, inorder)

    def buildSubTree(self, preorder, inorder):
        if preorder == []:
            return None

        root = TreeNode(preorder[0])

        index = inorder.index(root.val)
        left_preorder = preorder[1:index+1]
        right_preorder = preorder[index+1:]
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]

        root.left = self.buildSubTree(left_preorder, left_inorder)
        root.right = self.buildSubTree(right_preorder, right_inorder)

        return root
