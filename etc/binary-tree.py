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

    def DFS(self):
        print("--- DFS ---")
        # そのノードに辿り着いたら既読にするやつ
        def pre_order(node):
            print(node.val)
            if node.left:
                pre_order(node.left)
            if node.right:
                pre_order(node.right)

        # 左をチェックしたら既読にするやつ
        def pre_order(node):
            if node.left:
                pre_order(node.left)
            print(node.val)
            if node.right:
                pre_order(node.right)

        # 左右チェック終わったら既読にするやつ
        def pre_order(node):
            if node.left:
                pre_order(node.left)
            if node.right:
                pre_order(node.right)
            print(node.val)

        return pre_order(self.root)

    def BFS(self):
        print("--- BFS ---")
        q = [self.root]

        def left2right(q):
            laylength = len(q)
            for _ in range(laylength):
                nums = q.pop(0)
                print(nums.val)
                if nums.left:
                    q.append(nums.left)
                if nums.right:
                    q.append(nums.right)
            
            # 次のレイヤーがなくてもラスト一周回る
            # print("laylength:{}, len({})".format(laylength, len(q)))
            # こっちでも良さそうだが（問題によってはループに影響ある？）
            # if len(q) > 0:
            if laylength > 0:
                left2right(q)

        return left2right(q)

    def levelOrder(self, root):
        ans = []
        q = deque([root])
        
        def l2r(q):
            l = len(q)
            layer_val = []
            for _ in range(l):
                node = q.popleft()
                layer_val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(layer_val)
            if len(q) > 0:
                l2r(q)
        l2r(q)
        return ans


bt = BinaryTree()
l = [4, 2, 3, 1, 6, 5]
for _ in l:
    bt.add(_)

bt.DFS()
bt.BFS()

###################
#         4       #
#      /     \    #
#     2       6   #
#    / \     /    # 
#   1   3   5     # 
###################
