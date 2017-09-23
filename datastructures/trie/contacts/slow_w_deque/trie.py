from collections import defaultdict, deque

class TrieNode:

    def __init__(self):
        self.count = 0
        self.char_to_trie = defaultdict(TrieNode)

    def add(self, input_str):
        self.add_deque(deque(input_str))

    def add_deque(self, input_deque):
        first_char = input_deque.popleft()
        self.char_to_trie[first_char].count += 1
        if input_deque:
            self.char_to_trie[first_char].add_deque(input_deque)

    def find(self, partial_str):
        return self.find_deque(deque(partial_str))

    def find_deque(self, partial_deque):
        first_char = partial_deque.popleft()
        if partial_deque:
            return self.char_to_trie[first_char].find_deque(partial_deque)
        return self.char_to_trie[first_char].count

