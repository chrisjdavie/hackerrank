from collections import deque
import unittest

from contacts.trie import Trie

class TestTrie(unittest.TestCase):

    def test_char_to_node(self):

        this_trie = Trie()
        default_arg = this_trie.root.char_to_node["a"]
        self.assertEqual(default_arg.count, 0)

        default_arg.count += 1
        default_arg = this_trie.root.char_to_node["a"]
        self.assertEqual(default_arg.count, 1)
    
    def test_add_single_char(self):
        
        test_str = "a"

        this_trie = Trie()
        this_trie.add(test_str)

        self.assertEqual(this_trie.root.char_to_node[test_str].count, 1)

    def test_add_two_chars_twice(self):

        test_str = "ab"

        this_trie = Trie()
        this_trie.add(test_str)
        this_trie.add(test_str)

        self.assertEqual(this_trie.root.char_to_node[test_str[0]].count, 2)
        self.assertEqual(this_trie.root.char_to_node[test_str[0]].char_to_node[test_str[1]].count, 2)

    def test_add(self):
        test_str = "a"
        
        this_trie = Trie()
        this_trie.add(test_str)

        self.assertEqual(this_trie.root.char_to_node[test_str].count, 1)

    def test_find_single_char(self):
        
        test_str = "a"

        this_trie = Trie()
        this_trie.add(test_str)

        test_str_count = this_trie.find(test_str)
        self.assertEqual(test_str_count, 1)

    def test_find_two_chars_add_twice(self):

        test_str = "ab"

        this_trie = Trie()
        this_trie.add(test_str)
        this_trie.add(test_str)

        test_str_0_count = this_trie.find(test_str[0])
        self.assertEqual(test_str_0_count, 2)

        test_str_count = this_trie.find(test_str)
        self.assertEqual(test_str_count, 2)

    def test_find(self):

        test_str = "a"

        this_trie = Trie()
        this_trie.add(test_str)

        test_str_count = this_trie.find(test_str)
        self.assertEqual(test_str_count, 1)

