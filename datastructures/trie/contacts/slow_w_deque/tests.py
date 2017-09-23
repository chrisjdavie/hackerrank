from collections import deque
import unittest

from contacts.trie import TrieNode

class TestTrieNode(unittest.TestCase):

    def test_char_to_trie(self):

        this_trie = TrieNode()
        default_arg = this_trie.char_to_trie["a"]
        self.assertEqual(default_arg.count, 0)

        default_arg.count += 1
        default_arg = this_trie.char_to_trie["a"]
        self.assertEqual(default_arg.count, 1)
    
    def test_add_deque_single_char(self):
        
        test_str = "a"
        test_deque = deque(test_str)

        this_trie = TrieNode()
        this_trie.add_deque(test_deque)

        self.assertEqual(this_trie.char_to_trie[test_str].count, 1)

    def test_add_deque_two_chars_twice(self):

        test_str = "ab"
        test_deque0 = deque(test_str)
        test_deque1 = deque(test_str)

        this_trie = TrieNode()
        this_trie.add_deque(test_deque0)
        this_trie.add_deque(test_deque1)

        self.assertEqual(this_trie.char_to_trie[test_str[0]].count, 2)
        self.assertEqual(this_trie.char_to_trie[test_str[0]].char_to_trie[test_str[1]].count, 2)

    def test_add(self):
        test_str = "a"
        
        this_trie = TrieNode()
        this_trie.add(test_str)

        self.assertEqual(this_trie.char_to_trie[test_str].count, 1)

    def test_find_deque_single_char(self):
        
        test_str = "a"
        test_deque = deque(test_str)

        this_trie = TrieNode()
        this_trie.add(test_str)

        test_str_count = this_trie.find_deque(test_deque)
        self.assertEqual(test_str_count, 1)

    def test_find_deque_two_chars_add_twice(self):

        test_str = "ab"

        this_trie = TrieNode()
        this_trie.add(test_str)
        this_trie.add(test_str)

        test_str_0_count = this_trie.find_deque(deque(test_str[0]))
        self.assertEqual(test_str_0_count, 2)

        test_str_count = this_trie.find_deque(deque(test_str))
        self.assertEqual(test_str_count, 2)

    def test_find(self):

        test_str = "a"

        this_trie = TrieNode()
        this_trie.add(test_str)

        test_str_count = this_trie.find(test_str)
        self.assertEqual(test_str_count, 1)

