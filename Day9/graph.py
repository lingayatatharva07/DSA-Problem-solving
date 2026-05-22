#{A:[B,C,D],
#B:[A,E],
#C:[A,D],
#D:[A,C,E],
#E:[B,D]}

# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ':', self.adjacency_list[vertex])


# my_graph = Graph()

# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')
# my_graph.add_vertex('F')

# my_graph.print_graph()

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:

            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)

            del self.adjacency_list[vertex]
            return True

        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])


# Create Graph
my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")

print("Before Removing:")
my_graph.print_graph()

my_graph.remove_vertex("D")

print("\nAfter Removing D:")
my_graph.print_graph()