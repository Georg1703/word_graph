from main import Node
from main import WordGraph

def test_adding_neighbors():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.add_neighbors([b])
    a.add_neighbors([c])

    assert a.neighbors == [b, c]

def test_get_words():
    r = Node('r')
    o = Node('o')
    m = Node('m')

    r.add_neighbors([o])
    o.add_neighbors([m, r])
    m.add_neighbors([o])

    graph = WordGraph()
    graph.add_node(r)
    graph.add_node(o)
    graph.add_node(m)

    assert graph.get_words() == ['rom']

if __name__ == '__main__':
    test_get_words()
    test_adding_neighbors()