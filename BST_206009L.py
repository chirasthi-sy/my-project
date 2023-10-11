class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value


#defining traverse function
def traverse(self):
    if self:
        traverse(self.left)
        print(self.key)
        traverse(self.right)

#defining insert function
def insert(self, value):
    if self is None:
        return Node(value)
    else:
        if self.key < value:
            self.right = insert(self.right, value)
        else:
            self.left = insert(self.left, value)
    return self

#defining search function for binary search tree
def search(self,value):
    while self != None:
        if value > self.key:
            self = self.right
        elif value < self.key:
            self = self.left
        else:
            return True
    return False
    
#inserting the values to the tree
s = Node(20)
insert(s,40)
insert(s,10)
insert(s,4)
insert(s,15)
insert(s,50)
insert(s,35)
insert(s,55)
insert(s,60)


#traversing the tree
print(traverse(s))

#searching for 15 in binary search tree
print(search(s,15))

#searching for 52 in binary search tree
print(search(s,52))


print("New Code added")
