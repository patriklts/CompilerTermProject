class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):             # Add a child to the node
        self.children.append(child)

    def add_child_at(self, child, index):   # Add a child to the node at a specific index
        self.children.insert(index, child)
    
    def remove_child(self, child):          # Remove a child from the node
        self.children.remove(child)

    def get_children(self):                 # Return the children of the node as a list
        return self.children

    def get_data(self):                     # Return the data of the node                     
        return self.data
    
    def print_tree(self, level=0, indent="", is_last=False):
        prefix = "└── " if is_last else "├── "      # create a prefix for vertical lines 
        vertical_line = "   " if is_last else "|  "
        if level == 0:  # root node
            print(f'{self.get_data()}') # print the root node
        else:
            print(f'{indent}{prefix}{self.get_data()}') # print children with prefix allignment 
    
        indent += vertical_line # increase the indent for the next children
        for i, child in enumerate(self.get_children()): # recursivly print the children
            child.print_tree(level + 1, indent, i == len(self.get_children()) - 1)