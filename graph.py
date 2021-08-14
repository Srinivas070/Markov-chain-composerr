# This is our Markov Chain Representation

import random

# Define the graph in terms of vertices

class Vertex:
    def __init__(self,value) : # value will be the word 
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbours = []
        self.neighbours_weights = []


    def add_edge_to(self, vertex, weight=0):
        # This is adding an edge in the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self , vertex):
        # This is incrementing the weight of the edge 
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_nap(self):
        for (vertex,weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbours_weights.append(weight)


    def next_word(self):
        # Randomly select next word *** Based on weights!!!
        return random.choices(self.neighbours,weights = self.neighbours_weights)[0]


# Now that we have our vertex representation ,we put this together in a graph

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # What are the values of all the vertices?
        # in other words, return all possible words
        return set (self.vertices.keys()) 

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # What if the value isnt in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices(value) # get the vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()


