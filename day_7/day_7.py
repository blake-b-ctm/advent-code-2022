# partially implement file tree with cd commands

from collections import defaultdict

class Tree(defaultdict):
    def __call__(self):
        return Tree(self)

    def __init__(self, parent):
        self.parent = parent
        self.default_factory = self

root = Tree(['root'])
currentNode = root

currentNode['a'] = Tree([123, 456])
currentNode['d'] = Tree(None)
currentNode = root['a']
currentNode['e'] = Tree(None)
print('root => ', root)
print('currentNode =>', currentNode)
print('dir a parent =>', currentNode.parent)
    