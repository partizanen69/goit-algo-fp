# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

# - Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.
# - Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.
# - Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.

class Node:
  def __init__(self, data: int | None = None) -> None:
    self.data: int | None = data
    self.next: Node | None = None


class LinkedList:
  def __init__(self) -> None:
    self.head: Node | None = None

  def insert_at_beginning(self, data: int) -> None:
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data: int) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node | None, data: int) -> None:
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int) -> None:
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self) -> None:
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse_list(self) -> None:
    prev = None
    current = self.head

    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev
    
  def sort_list(self) -> None:
    if not self.head or not self.head.next:
      return

    sorted_head = None
    current = self.head

    while current:
      next_node = current.next
        
      if not sorted_head or sorted_head.data >= current.data:
        current.next = sorted_head
        sorted_head = current
      else:
        temp = sorted_head
        while temp.next and temp.next.data < current.data:
          temp = temp.next
        current.next = temp.next
        temp.next = current
      
      current = next_node

    self.head = sorted_head
  
  def merge_sorted_lists(self, other_list: 'LinkedList') -> None:
    if not other_list.head:
      return
    if not self.head:
      self.head = other_list.head
      return

    self.sort_list()
    other_list.sort_list()

    dummy = Node(0)
    tail = dummy
    
    list1 = self.head 
    list2 = other_list.head

    while list1 and list2:
      if list1.data <= list2.data:
        tail.next = list1
        list1 = list1.next
      else:
        tail.next = list2
        list2 = list2.next
      tail = tail.next

    if list1:
      tail.next = list1
    if list2:
      tail.next = list2

    self.head = dummy.next

if __name__ == "__main__":
  # Create first linked list
  list1 = LinkedList()
  list1.insert_at_end(1)
  list1.insert_at_end(2)
  list1.insert_at_end(3)
  print("Original list:")
  list1.print_list()  # Expected output: 1 -> 2 -> 3

  list1.reverse_list()
  print("\nReversed list:")
  list1.print_list()  # Expected output: 3 -> 2 -> 1

  # Example of sort_list
  print("\nOriginal unsorted list:")
  list1 = LinkedList()
  list1.insert_at_end(3)
  list1.insert_at_end(1) 
  list1.insert_at_end(4)
  list1.insert_at_end(2)
  list1.print_list()  # Expected output: 3 -> 1 -> 4 -> 2

  list1.sort_list()
  print("\nSorted list:")
  list1.print_list()  # Expected output: 1 -> 2 -> 3 -> 4

  # Example of merge_sorted_lists
  print("\nMerging two sorted lists:")
  list1 = LinkedList()
  list2 = LinkedList()
  
  # Create first sorted list: 1 -> 3 -> 5
  list1.insert_at_end(1)
  list1.insert_at_end(3)
  list1.insert_at_end(5)
  print("First sorted list:")
  list1.print_list()
  
  # Create second sorted list: 2 -> 4 -> 6
  list2.insert_at_end(2)
  list2.insert_at_end(4)
  list2.insert_at_end(6)
  print("Second sorted list:")
  list2.print_list()
  
  list1.merge_sorted_lists(list2)
  print("Merged sorted list:")
  list1.print_list()  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
