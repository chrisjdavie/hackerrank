
import sys

from .grid import BuildGrid, play

grid, castle, target = BuildGrid.from_hackerrank_input(sys.stdin)
print(play(grid,castle,target))
