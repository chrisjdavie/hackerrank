
from .brackets import Brackets

N = int(input())

for _ in range(N):
    bracket_str = str(input())
    brk = Brackets(bracket_str)
    if brk.balanced():
        print("YES")
    else:
        print("NO")

