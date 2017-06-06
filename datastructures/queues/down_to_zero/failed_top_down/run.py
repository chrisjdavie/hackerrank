from .game_stuff import play

Q = int(input())

for _ in range(Q):
    N = int(input())
    print(play(N))

