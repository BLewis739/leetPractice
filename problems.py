from asyncio.windows_events import NULL
from tkinter import Y


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For testing purposes, initialize a few trees


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

z = TreeNode(1)
y = TreeNode(2)
x = TreeNode(2)
w = TreeNode(3)
v = TreeNode(3)

z.left = y
z.right = x
y.right = w
x.right = v

#
# 101
# Symmetric Tree
#


def isSymmetric(root):
    if root.left.val != root.right.val:
        return False
    else:
        layerL = []
        layerR = []
        layerL.append(
            root.left.left.val) if root.left.left else layerL.append(None)
        layerL.append(
            root.left.right.val) if root.left.right else layerL.append(None)
        layerR.append(
            root.right.right.val) if root.right.right else layerR.append(None)
        layerR.append(
            root.right.left.val) if root.right.left else layerR.append(None)
        print(layerL)
        print(layerR)


isSymmetric(z)
