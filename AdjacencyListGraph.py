ADJACENCY LIST IMPLEMENTATION
---------------------------------------------------------------------------------------------------------
DATA STRUCTURE: DICTIONARY
--------------------------  
    class AdjacencyList:
    def __init__(self, N, M):
        self.nodes_num = N
        self.edges_num = M
        self.adjList = dict()
    
    def edges(self, from_, to_):
        if from_ not in self.adjList:
            self.adjList[from_] = [to_]
            # undirected edge is specified in problem
        else:
            self.adjList[from_].append(to_)
        if to_ not in self.adjList:
            self.adjList[to_] = [from_]
        else:
            self.adjList[to_].append(from_)
    def find_edge(self, from_, to_):
        for i in (self.adjList[from_]):
            if i==to_:
                return "YES"
        return 'NO'
n, m = map(int, input().split())
adjacency_list = AdjacencyList(n, m)
for i in range(m):
    A, B = input().split()
    adjacency_list.edges(A, B)
q = int(input())
for i in range(q):
    c, d = input().split()
    print(adjacency_list.find_edge(c, d))
    #print(adjacency_list.adjList)




DATA STRUCTURE: LINKED LIST
-------------------------------
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, V):
        self.v = V
        self.graph = [None]*self.v

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        print("self.graph",
              self.graph[src], self.graph[src].vertex, self.graph[src].next)
        # In case of Undirected Graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.v):
            current = self.graph[i]
            print("Head->", end='')
            while current:
                print("->{}".format(current.vertex),
                      end='')
                current = current.next
            print()

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
