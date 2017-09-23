
from contacts.trie import TrieNode

N = int(input())

trie = TrieNode()

for _ in range(N):
    instruct, in_str = input().split()
    if instruct == "add":
        trie.add(in_str)
    if instruct == "find":
        print(trie.find(in_str))

