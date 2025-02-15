# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
# використовуючи бінарну купу. Завдання включає створення графа за допомогою бібліотеки networkx,
# використання піраміди 
# для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
# - Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у 
# графі з використанням бінарної купи (піраміди).
# - У межах реалізації завдання створено граф, використано піраміду для оптимізації
# вибору вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Set, Tuple, List

def dijkstra(graph: nx.Graph, start: int) -> Tuple[Dict[int, float], Dict[int, int]]:
  distances: Dict[int, float] = {node: float('infinity') for node in graph.nodes()}
  distances[start] = 0
  predecessors: Dict[int, int] = {node: None for node in graph.nodes()}
  
  pq: List[Tuple[int, int]] = [(0, start)]
  visited: Set[int] = set()
  
  while pq:
    current_distance, current_vertex = heapq.heappop(pq)
    
    if current_vertex in visited:
      continue
      
    visited.add(current_vertex)
    
    for neighbor in graph.neighbors(current_vertex):
      if neighbor in visited:
        continue
        
      weight = graph[current_vertex][neighbor]['weight']
      distance = current_distance + weight
      
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        predecessors[neighbor] = current_vertex
        heapq.heappush(pq, (distance, neighbor))
        
  return distances, predecessors

def create_sample_graph() -> nx.Graph:
  G = nx.Graph()
  edges: Tuple[int, int, int] = [
    (0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5),
    (2, 3, 8), (2, 4, 10), (3, 4, 2), (3, 5, 6),
    (4, 5, 3)
  ]
  G.add_weighted_edges_from(edges)
  
  return G

if __name__ == "__main__":
  G = create_sample_graph()
  pos = nx.spring_layout(G)
  
  nx.draw(G, pos, with_labels=True, node_color='lightblue', 
          node_size=500, font_size=16, font_weight='bold')
  
  edge_labels = nx.get_edge_attributes(G, 'weight')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
  
  start_vertex = 0
  distances, predecessors = dijkstra(G, start_vertex)
  
  print(f"\nShortest distances from vertex {start_vertex}:")
  for vertex in sorted(distances.keys()):
    print(f"To vertex {vertex}: {distances[vertex]}")
  
  plt.show()
