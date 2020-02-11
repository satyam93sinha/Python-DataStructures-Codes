# Adjacency List Implementation:
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
