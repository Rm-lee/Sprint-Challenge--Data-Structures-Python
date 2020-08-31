import time
import sys
sys.setrecursionlimit(15000)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n").strip() # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n").strip() # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

class Tree:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

    def insert(self,name):
        if ord(name[0].lower()) >= ord(self.name[0].lower()):
            if self.right is None:
                new_node = Tree(name)
                self.right = new_node
            else:
                self.right.insert(name)

        if ord(name[0].lower()) < ord(self.name[0].lower()):
            if self.left is None:
                self.left = Tree(name)
            else:
                self.left.insert(name)
    def get_dups(self, target):
        
        if target == self.name:
            duplicates.append(target)
        if ord(target[0].lower()) > ord(self.name[0].lower()):
            if self.right is None:
                return 
            else:
                return self.right.get_dups(target)

        if ord(target[0].lower()) < ord(self.name[0].lower()):
            if self.left is None:
                return 
            else:
                return self.left.get_dups(target)  
new_tree = Tree("tim")
for name_1 in names_1:
    new_tree.insert(name_1.strip())
for name_2 in names_2:
    new_tree.get_dups(name_2.strip())
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
