# basic

from collections import deque

# node definition
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    # 初期値 None
    def __init__(self):
        self.root = None

    def add(self, val):
        def add_node(root, val):
            if val < root.val:
                if not root.left:
                    root.left = Node(val)
                else:
                    add_node(root.left, val)
            else:
                if not root.right:
                    root.right = Node(val)
                else:
                    add_node(root.right, val)
        
        # root が空なら最初のNodeを構築
        if not self.root:
            self.root = Node(val)
        else:
            add_node(self.root, val)

bt = BinaryTree()
l = [4, 2, 3, 1, 6, 5]
for _ in l:
    bt.add(_)

###################
#         4       #
#      /     \    #
#     2       6   #
#    / \     /    # 
#   1   3   5     # 
###################
