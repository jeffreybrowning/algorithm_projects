# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    values = set()
    stack = []
    while stack:
        node = stack.pop()
        # check for dupes
        if node.data in values:
            return False
        values.add(node.data)

        # if its a leaf
        if not node.left and not node.right:
            continue

        if node.data > node.left and node.data < node.right:
            stack.append(node.left)
            stack.append(node.right)
        else:
            return False

    return True