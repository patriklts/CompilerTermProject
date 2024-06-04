class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data
    
    def add_parent(self, parent):
        self.parent = parent
        parent.add_child(self)
        
    def remove_parent(self):
        self.parent.remove_child(self)
        self.parent = None