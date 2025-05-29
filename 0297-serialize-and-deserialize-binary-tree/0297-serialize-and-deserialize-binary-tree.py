# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ## use level order traversal and then convert it into a string joining with a delimiter
        if not root:
            return ""
        ans = []
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr:
                ans.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                ans.append("null")
        return ",".join(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q and i < len(nodes):
            curr = q.popleft()
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1

            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1
        
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))