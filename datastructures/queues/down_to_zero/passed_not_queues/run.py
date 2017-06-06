
from .play import setup_struct

n = int(input())
target_vals_set = set()
target_vals_list = []
for _ in range(n):    
    m = int(input())
    target_vals_set.add(m)  
    target_vals_list.append(m)
moves = setup_struct(target_vals_set)

print('foo')
print(max(target_vals_list))
for tv in target_vals_list:
    print(tv, moves[tv])
    exit()
    

