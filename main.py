from typing import List, Self

class Node:
    def __init__(self, character: str):
        self.character = character
        self._neighbors = []
    
    def add_neighbors(self, neighbors: List[Self]):
        self._neighbors.extend(neighbors)

    @property
    def neighbors(self) -> List[Self]:
        return self._neighbors


class WordGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, new_node):
        self.nodes[new_node] = new_node
    
    def is_word(self, word):
        return  word in ['pop', 'rom', 'corn', 'popcorn', 'rock', 'mock', 'ok']

    def get_words(self):
        words = []

        def dfs(node, path, used_edges):
            new_path = path + node.character
            if self.is_word(new_path):
                words.append(new_path)

            for neighbor_id in self.nodes[node].neighbors:
                edge = (node.character, neighbor_id.character)
                if edge not in used_edges:
                    new_used_edges = set(used_edges)
                    new_used_edges.add(edge)
                    dfs(neighbor_id, new_path, new_used_edges)


        for node in self.nodes:
            dfs(node, "", set())

        return sorted(set(words))


p1 = Node('p')
p2 = Node('p')
o1 = Node('o')
c = Node('c')
n = Node('n')
o2 = Node('o')
k = Node('k')
r = Node('r')
m = Node('m')

p1.add_neighbors([p2, o1])
p2.add_neighbors([p1, o1, c])
o1.add_neighbors([p1, p2, n])
c.add_neighbors([p2, o2, k])
n.add_neighbors([o1, r])
r.add_neighbors([n, o2])
o2.add_neighbors([r, m, k, c])
m.add_neighbors([o2])
k.add_neighbors([o2, c])

graph = WordGraph()
graph.add_node(p1)
graph.add_node(p2)
graph.add_node(o1)
graph.add_node(c)
graph.add_node(o2)
graph.add_node(n)
graph.add_node(r)
graph.add_node(m)
graph.add_node(k)

if __name__ == '__main__':
    print(graph.get_words())