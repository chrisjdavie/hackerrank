from collections import defaultdict


class Node:

    def __init__(self):
        self.count = 0
        self.char_to_node = defaultdict(Node)


class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, input_str):
        node = self.root
        for a_char in input_str:
            node = node.char_to_node[a_char]
            node.count += 1

    def find(self, partial_str):
        node = self.root
        for a_char in partial_str:
            node = node.char_to_node[a_char]
            # this if stops it as soon as the partial is not present, instead
            # of exploring to the end of the word (allowed due to defaultdict 
            # recursion). Required to pass tests.
            if not node.count:
                break
        return node.count

