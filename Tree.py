import math

######## Binary Tree 
class Node: 
    def __init__ (self, value=None):
        self.value = value
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):

        if self.root == None:
            self.root = Node(value)
        else:
            start = self.root
            while True:
                if start.value == value:
                    print("Tree cannot have same values")
                    break
                elif start.value < value:
                    if start.right == None:
                        start.right = Node(value)
                        break
                    else:
                        start = start.right
                elif start.value > value:
                    if start.left == None:
                        start.left = Node(value)
                        break
                    else:
                        start = start.left

    ### DFS Traversal 
    def DFS(self,input):
        self.output = ""
        def inorder(node):
            if node != None:  
                inorder(node.left)
                self.output += str(node.value) + ","
                inorder(node.right )
            else:
                return 

        def preorder(node):
            if node:
                self.output += str(node.value) + ","
                preorder(node.left)
                preorder(node.right)
            else:
                return

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                self.output += str(node.value) + ","
            else:
                return 

        if input == "inorder":
            inorder(self.root)
            print("Inorder :", self.output)
        elif input == "preorder":
            preorder(self.root)
            print("preorder :",self.output )
        elif input == "postorder":
            postorder(self.root)
            print("postorder :",self.output )
        else:
            print("invalid Input")

    ### DFS algo to find height of tree    
    def height(self):
        def maxDepth( node, currDepth=0): 
            if not node:
                return currDepth
            currDepth += 1
            return max(maxDepth(node.left, currDepth), maxDepth(node.right, currDepth))

        print("Height of Binary Tree :",maxDepth(self.root))

    ### Right side view of Tree (viewing tree from right side)
    def rightView(self):
        # NLR got reversed to NRL so that we can get right first 
        def reversedPreOrder(node, currLvl,result):
            if not node:
                return 
            if currLvl >= len(result):
                result.append(node.value)
            if node.right :
                reversedPreOrder(node.right,currLvl+1, result)
            if node.left :
                reversedPreOrder(node.left,currLvl+1, result)
        
        self.result = []
        reversedPreOrder(self.root, 0, self.result)
        print(self.result)

    ### BFS or Level Order Traversal
    def BFS(self):
        output = []
        q = [self.root]
        while len(q) != 0 : 
            curr = q.pop(0)
            output.append(curr.value)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        print(output)

    ### BFS : elements separated by lvls
    def Levels(self):
        output = []
        if not self.root:
            print(output)
            return 
        q = [self.root]
        while len(q): 
            l = len(q)
            count = 0 
            currLvl = []
            while count < l:
                curr = q.pop(0)
                currLvl.append(curr.value)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
                count += 1
            output.append(currLvl)
        print(output)

    ### RIght side tree view by BFS algo
    def rightViewBFS(self):
        output = []
        if not self.root:
            print(output)
            return

        q = [self.root]
        while len(q): 
            l = len(q)
            count = 0 
            currLvl = []
            while count < l:
                curr = q.pop(0)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
                count += 1
                if count == l:
                    output.append(curr.value)
        print(output)

    ### To check if the tree is binary search Tree or not
    def isBst(self):
        # DFS Algo
        def checkBST(node, min, max):
            if node is None:
                return True
            if node.value <= min or node.value >= max:
                return False
            if node.left: # checking if left not null
                # if we get false from checkBSt then we have to return false
                # for that we converting resulted false into true with the help 
                # of not so that if conditions works and we return False
                if not checkBST(node.left, min, node.value):
                    return False
            if node.right: # checking if right not null
                if not checkBST(node.right, node.value, max):
                    return False
            return True

        if checkBST(self.root, -math.inf, math.inf):
            print("True")
        else:
            print("False")


T1 = BinaryTree()

T1.insert(15)
T1.insert(12)
T1.insert(17)
T1.insert(14)
T1.insert(8)
T1.insert(9)
T1.insert(10)

# T1.DFS("inorder") # Inorder : 8,9,10,12,14,15,17,
# T1.DFS("preorder")# preorder : 15,12,8,9,10,14,17,
# T1.DFS("postorder")# postorder : 10,9,8,14,12,17,15,
# T1.DFS("inodjrder")# invalid Input
# T1.height() #Height of Binary Tree : 5
# T1.rightView() #[15, 17, 14, 9, 10]

# T1.BFS() # [15, 12, 17, 8, 14, 9, 10]
# T1.Levels() # [[15], [12, 17], [8, 14], [9], [10]]
# T1.rightViewBFS() [15, 17, 14, 9, 10]

# T1.isBst() # True
# T1.root.right.value = 5
# T1.isBst() # False




























































































































































