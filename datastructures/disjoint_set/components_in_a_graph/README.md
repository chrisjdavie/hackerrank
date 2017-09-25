Take from hackerrank, https://www.hackerrank.com/challenges/components-in-graph/problem

#Components in a graph

There are 2N values to represent nodes in a graph. They are divided into two sets G and B. Each set has exactly N values. Set G is represent by {G1, G2, .., GN}. G can contain any value between 1 to N (inclusive). Set B is represented by {B1, B2, ..., BN}. B can contain any value between N+1 to N (inclusive). Same value can be chosen any number of times.

Here (G1, B1), (G2, B2), ... (GN, BN) represents the edges of the graph.

Your task is to print the number of vertices in the smallest and the largest connected components of the graph.

*Note* Single nodes should not be considered in the answer.

For more clarity look at the following figure.

<img src="http://mathforum.org/mathimages/imgUpload/thumb/Tree_graph.jpg/500px-Tree_graph.jpg">

For the above graph smallest connected component is 7 and largest connected component is 17.

##Input Format

First line contains an integer N.
Each of the next N lines contain two space-separated integers, ith line contains Gi and Bi.

##Constraints

1<=N<=15000
1<=Gi<=N
N+1<=Bi<=2N

##Output Format

Print two space separated integers, the number of vertices in the smallest and the largest components.

Sample Input

5
1 6 
2 7
3 8
4 9
2 6

Sample Output

2 4

Explanation

The number of vertices in the smallest connected component in the graph is 2 i.e. either (3,8) or (4,9).
The number of vertices in the largest connected component in the graph is 4 i.e. 1 - 2 - 6 - 7.


