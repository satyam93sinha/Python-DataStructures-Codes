Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [None]*5
[None, None, None, None, None]
>>> 
======== RESTART: G:/ProgramsPython/Algorithms/AdjacencyListGraph.py ========
self.graph <__main__.AdjNode object at 0x04177C10> 1 None
self.graph <__main__.AdjNode object at 0x04177C30> 4 <__main__.AdjNode object at 0x04177C10>
self.graph <__main__.AdjNode object at 0x04177DB0> 3 None
self.graph <__main__.AdjNode object at 0x04177DF0> 4 <__main__.AdjNode object at 0x04177DB0>
self.graph <__main__.AdjNode object at 0x04177E30> 2 <__main__.AdjNode object at 0x04177DF0>
self.graph <__main__.AdjNode object at 0x04177C90> 3 None
self.graph <__main__.AdjNode object at 0x04186190> 4 None
>>> graph.graph[0]
<__main__.AdjNode object at 0x04177C30>
>>> graph.graph[0].vertex
4
>>> graph.graph[0].next.vertex
1
>>> graph.graph[1].vertex
2
>>> graph.graph[1].next.vertex
4
>>> graph.graph[1].next.next.vertex
3
>>> graph.graph[0].next.next
>>> 
======== RESTART: G:/ProgramsPython/Algorithms/AdjacencyListGraph.py ========
self.graph <__main__.AdjNode object at 0x03747C70> 1 None
self.graph <__main__.AdjNode object at 0x03747C30> 4 <__main__.AdjNode object at 0x03747C70>
self.graph <__main__.AdjNode object at 0x03747DF0> 3 None
self.graph <__main__.AdjNode object at 0x03747E30> 4 <__main__.AdjNode object at 0x03747DF0>
self.graph <__main__.AdjNode object at 0x03747E70> 2 <__main__.AdjNode object at 0x03747E30>
self.graph <__main__.AdjNode object at 0x03747C50> 3 None
self.graph <__main__.AdjNode object at 0x0375A1D0> 4 None
>>> graph.print_graph()
Head->->4->1
Head->->2->4->3
Head->->3
Head->->4
Head->
>>> 
======== RESTART: G:/ProgramsPython/Algorithms/AdjacencyListGraph.py ========
self.graph <__main__.AdjNode object at 0x03BE7BD0> 1 None
self.graph <__main__.AdjNode object at 0x03BE7DB0> 4 <__main__.AdjNode object at 0x03BE7BD0>
self.graph <__main__.AdjNode object at 0x03BE7E30> 3 <__main__.AdjNode object at 0x03BE7BF0>
self.graph <__main__.AdjNode object at 0x03BF61B0> 4 <__main__.AdjNode object at 0x03BE7E30>
self.graph <__main__.AdjNode object at 0x03BF6250> 2 <__main__.AdjNode object at 0x03BF61B0>
self.graph <__main__.AdjNode object at 0x03BF6290> 3 <__main__.AdjNode object at 0x03BF6190>
self.graph <__main__.AdjNode object at 0x03BF62D0> 4 <__main__.AdjNode object at 0x03BF61D0>
>>> graph.print_graph()
Head->->4->1
Head->->2->4->3->0
Head->->3->1
Head->->4->2->1
Head->->3->1->0
>>> 
