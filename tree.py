class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_child_at(self, child, index):
        self.children.insert(index, child)
    
    def remove_child(self, child):
        self.children.remove(child)

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data
    
    def print_tree(self, level=0, indent="", is_last=False):
        prefix = "└── " if is_last else "├── "
        vertical_line = "   " if is_last else "|  "
        if level == 0:  # root node
            print(f'{self.get_data()}')
        else:
            print(f'{indent}{prefix}{self.get_data()}')
    
        indent += vertical_line
        for i, child in enumerate(self.get_children()):
            child.print_tree(level + 1, indent, i == len(self.get_children()) - 1)