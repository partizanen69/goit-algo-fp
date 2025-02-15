import uuid
import networkx as nx
import matplotlib.pyplot as plt
from typing import List
import heapq

class Node:
    def __init__(self, key: int, color: str = "skyblue") -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.val: int = key
        self.color: str = color  # Додатковий аргумент для зберігання кольору вузла
        self.id: str = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph: nx.DiGraph, node: Node | None, pos: dict[str, tuple[float, float]], 
             x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node) -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == "__main__":
    # create heap
    heap_arr: List[int] = [15, 8, 23, 4, 42, 16, 7, 31, 12, 35, 19, 27, 3, 11, 38, 9, 44, 21, 5, 33, 14, 29, 6, 40, 17, 25, 10, 36, 2, 13]
    heapq.heapify(heap_arr)
    
    
    # build binary tree from heap
    nodes = [Node(val) for val in heap_arr]
    length = len(nodes)

    for i in range(length // 2):
        if 2 * i + 1 < length:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < length:
            nodes[i].right = nodes[2 * i + 2]
    
    # draw tree
    draw_tree(nodes[0])
    
    
    
    
    