from collections import deque
import queue
class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = []
        self.queue = deque()

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")


    def bfs(self, src):
        self.visited = [False for i in range(len(self.graph.keys())+1)]
        self.queue.append(src)
        while self.queue:
            front = self.queue.popleft()
            if not self.visited[front]:
                self.visited[front] = True
                print(front, end=' ->')
                for nxt in self.graph[front]:
                    self.queue.append(nxt)
            
    def dfs(self, src):
        if not self.visited[src]:
            self.visited[src] = True
            print(src, end='->')
            for nxt in self.graph[src]:
                self.dfs(nxt)
    
    def print_dfs(self, src):
        self.visited = [False for i in range(len(self.graph.keys())+1)]
        self.dfs(1)
        
        
        

# undirected 
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 3)
graph.add_edge(5, 6)
graph.add_edge(6, 3)
graph.display()

print("BFS graph traversal : ")
graph.bfs(1)


print("\nDFS graph traversal : ")
graph.print_dfs(1)