def threeSum(nums):
    if len(nums) < 3:
        return []
    else:
        allArrs = []
        for i in range(len(nums)-2):
            firstTarget = nums[i]
            for j in range(1, len(nums)-1):
                if i < j:
                    secondTarget = nums[j]
                    for k in range(2, len(nums)):
                        if j < k:
                            thirdTarget = nums[k]
                            print([firstTarget, secondTarget, thirdTarget])
                            if firstTarget + secondTarget + thirdTarget == 0:
                                if len(allArrs) > 0:
                                    print("firstTarget " + str(firstTarget))
                                    addIt = True
                                    for z in range(len(allArrs)):
                                        print("All Arrs index " +
                                              str(z))
                                        print(allArrs[z])
                                        if firstTarget in allArrs[z]:
                                            print('ho')
                                            if secondTarget in allArrs[z]:
                                                print('hey')
                                                if thirdTarget in allArrs[z]:
                                                    print("Already in")
                                                    addIt = False
                                                    break
                                    if addIt:
                                        allArrs.append(
                                            [firstTarget, secondTarget, thirdTarget])
                                        print("All Arrs")
                                        print(allArrs)
                                else:
                                    allArrs.append(
                                        [firstTarget, secondTarget, thirdTarget])
                                    print("All Arrs")
                                    print(allArrs)
        return allArrs


testList = [-1, 0, 1, 2, -1, -4]

print(threeSum(testList))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # For testing purposes, initialize a few trees


# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(2)
# d = TreeNode(3)
# e = TreeNode(4)
# f = TreeNode(4)
# g = TreeNode(3)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g

# z = TreeNode(1)
# y = TreeNode(2)
# x = TreeNode(2)
# w = TreeNode(3)
# v = TreeNode(3)

# z.left = y
# z.right = x
# y.right = w
# x.right = v

# #
# # 101
# # Symmetric Tree
# #


# def treeScanner(root):
#     if not (root.left and root.right):
#         return [root.val]
#     else:
#         newlist = [root.val]
#         left = treeScanner(root.left)
#         right = treeScanner(root.right)
#         return newlist + left + right


# print(treeScanner(a))


# def isSymmetric(root):
#     if root.left.val != root.right.val:
#         return False
#     else:
#         layerL = []
#         layerR = []
#         layerL.append(
#             root.left.left.val) if root.left.left else layerL.append(None)
#         layerL.append(
#             root.left.right.val) if root.left.right else layerL.append(None)
#         layerR.append(
#             root.right.right.val) if root.right.right else layerR.append(None)
#         layerR.append(
#             root.right.left.val) if root.right.left else layerR.append(None)
#         print(layerL)
#         print(layerR)


# # isSymmetric(z)
