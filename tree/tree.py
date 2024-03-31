class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def searchBST(self, val: int, root: TreeNode) -> TreeNode:
        """查找结点迭代法"""
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None

    def searchBST2(self, val: int, root: TreeNode) -> TreeNode:
        """查找结点递归法"""
        if not root or val == root.val:
            return root
        if val < root.val:
            return self.searchBST2(val, root.left)
        if val > root.val:
            return self.searchBST2(val, root.right)

    def searchIntoBST(self, val: int, root: TreeNode) -> TreeNode:
        """递归插入结点并返回整个树,实际上只有末端结点返回值改变了上一级结点的指针值,其余层的指针值都无变化"""
        if root is None:
            node = TreeNode(val)
            return node
        if val < root.val:
            root.left = self.searchIntoBST(val, root.left)
        elif val > root.right:
            root.right = self.searchIntoBST(val, root.right)
        return root

    def searchBST(self, val: int, root: TreeNode) -> TreeNode:
        """迭代插入结点"""
        if root is None:
            root = TreeNode(val)
            return root

        parent = root
        cur = root
        while cur:
            parent = cur
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right

        if val < cur.val:
            parent.left = TreeNode(val)
        elif val > cur.val:
            parent.right = TreeNode(val)
        return root

    def inordertraverse(self, val, root) -> TreeNode:
        """对二叉树进行中序遍历，搜索树可以直接输出排序序列"""
        st = [] # 操作栈
        cur = root
        while cur is not None or st:
            while cur is not None:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            # 对cur.val进行操作
            cur = cur.right
        return












