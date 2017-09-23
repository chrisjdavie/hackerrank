
from contacts.trie import Trie

N = int(input())

trie = Trie()

for _ in range(N):
    instruct, in_str = input().split()
    if instruct == "add":
        trie.add(in_str)
    if instruct == "find":
        print(trie.find(in_str))

