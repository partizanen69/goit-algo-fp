# Завдання 5. Візуалізація обходу бінарного дерева
# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити 
# програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
# Вона повинна відображати кожен крок у вузлах з різними кольорами, 
# використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися
# від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при
# його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
# 👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

from collections import deque
import colorsys
from task4 import arr_to_heap_to_tree, draw_tree, Node
from typing import List

def generate_color(step: int, total_steps: int) -> str:
    hue = 0.6  # Blue hue
    saturation = 0.8
    value = 0.3 + (0.7 * step / total_steps)  # Value goes from 0.3 to 1.0
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

def bfs_traversal(root: Node | None) -> None:
    if not root:
        return
    
    queue: deque[Node] = deque([root])
    visited: list[Node] = []
    
    while queue:
        node = queue.popleft()
        visited.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    for i, node in enumerate(visited):
        node.color = generate_color(i, len(visited))
        
    draw_tree(root)
    
def dfs_traversal(root: Node | None) -> None:
    if not root:
        return
        
    stack = [root]
    visited = []
    
    while stack:
        node = stack.pop()
        visited.append(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    for i, node in enumerate(visited):
        node.color = generate_color(i, len(visited))
        
    draw_tree(root)


if __name__ == "__main__":
    arr: List[int] = [15, 8, 23, 4, 42, 16, 7, 31, 12, 35, 19, 27, 3, 11, 38, 9, 44, 21, 5, 33, 14, 29, 6, 40, 17, 25, 10, 36, 2, 13]
    root_node = arr_to_heap_to_tree(arr)
    
    print("BFS Traversal:")
    bfs_traversal(root_node)
    
    print("\nDFS Traversal:")
    dfs_traversal(root_node)
    
    
    