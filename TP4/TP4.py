class Binary_tree():
    def __init__(self):
        self.root = None


class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.depth = 0

    def add(self, left=None, right=None):
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self):
        retour = str(self)
        if self.right:
            retour += " " + self.right.display_node()
        if self.left:
            retour += " " + self.left.display_node()
        return retour

    def __str__(self):
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        # return self.left == None and self.right == None
        return not (self.left or self.right)

    def get_max_depth(self, max_depth=0):
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        # je suis le node d'un arbre
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)

            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth

    def printTree(self, depth=0):
        '''
         print the nodes in an organized tree
        '''
        retour = str(self)
        if self.right:
            retour += "\n"
            for i in range(0, depth + 1):
                retour += "\t"
            retour += self.right.printTree(depth + 1)
        if self.left:
            retour += "\n"
            for i in range(0, depth + 1):
                retour += "\t"
            retour += self.left.printTree(depth + 1)
        return retour


node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node3.add(node4)
node1.add(node2, node3)
tree1 = Binary_tree()
tree1.root = node1

node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node5.add(node6, node7)
node4.add(node5)
node8 = Node(8)
node7.add(node8)

print(node1.printTree())