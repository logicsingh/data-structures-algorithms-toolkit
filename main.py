"""Menu-driven command-line interface for the DSA Toolkit."""
from dsa_toolkit.searching import linear_search,binary_search
from dsa_toolkit.sorting import bubble_sort,selection_sort,insertion_sort,merge_sort
from dsa_toolkit.stack import Stack
from dsa_toolkit.queue import Queue
from dsa_toolkit.linked_list import LinkedList
from dsa_toolkit.binary_search_tree import BinarySearchTree

def integer_list(prompt="Enter integers separated by spaces: "):
    raw=input(prompt).strip()
    if not raw: return []
    try: return [int(x) for x in raw.split()]
    except ValueError: print("Please enter whole numbers separated by spaces."); return None

def search_demo():
    values=integer_list()
    if values is None: return
    try: target=int(input("Number to find: "))
    except ValueError: print("Please enter a whole number."); return
    print("Linear search index:",linear_search(values,target))
    print("Binary search index (uses sorted input):",binary_search(sorted(values),target))

def sort_demo():
    values=integer_list()
    if values is None: return
    print("1 Bubble | 2 Selection | 3 Insertion | 4 Merge")
    options={"1":("Bubble sort",bubble_sort),"2":("Selection sort",selection_sort),"3":("Insertion sort",insertion_sort),"4":("Merge sort",merge_sort)}
    choice=input("Algorithm: ").strip()
    if choice not in options: print("Invalid choice."); return
    name,fn=options[choice]; print(name+" result:",fn(values)); print("Original list:",values)

def stack_demo():
    s=Stack()
    while True:
        print("\nStack LIFO: 1 Push | 2 Pop | 3 Peek | 4 View | 0 Back")
        c=input("Choice: ").strip()
        if c=="0": return
        try:
            if c=="1": s.push(input("Value: "))
            elif c=="2": print("Popped:",s.pop())
            elif c=="3": print("Top:",s.peek())
            elif c=="4": print("Bottom to top:",s.to_list())
            else: print("Invalid choice.")
        except IndexError as e: print("Error:",e)

def queue_demo():
    q=Queue()
    while True:
        print("\nQueue FIFO: 1 Enqueue | 2 Dequeue | 3 Front | 4 View | 0 Back")
        c=input("Choice: ").strip()
        if c=="0": return
        try:
            if c=="1": q.enqueue(input("Value: "))
            elif c=="2": print("Dequeued:",q.dequeue())
            elif c=="3": print("Front:",q.front())
            elif c=="4": print("Front to back:",q.to_list())
            else: print("Invalid choice.")
        except IndexError as e: print("Error:",e)

def linked_list_demo():
    linked=LinkedList()
    while True:
        print("\nLinked list: 1 Append | 2 Prepend | 3 Find | 4 Delete | 5 View | 0 Back")
        c=input("Choice: ").strip()
        if c=="0": return
        if c=="1": linked.append(input("Value: "))
        elif c=="2": linked.prepend(input("Value: "))
        elif c=="3": print("Index:",linked.find(input("Value to find: ")))
        elif c=="4": print("Deleted." if linked.delete(input("Value to delete: ")) else "Value not found.")
        elif c=="5": print(linked.to_list(),"| Size:",linked.size())
        else: print("Invalid choice.")

def bst_demo():
    values=integer_list("Enter integers to insert into the tree: ")
    if values is None: return
    tree=BinarySearchTree()
    for value in values: tree.insert(value)
    while True:
        print("\nBST: 1 Search | 2 Inorder | 3 Preorder | 4 Postorder | 0 Back")
        c=input("Choice: ").strip()
        if c=="0": return
        if c=="1":
            try: print("Found." if tree.search(int(input("Number: "))) else "Not found.")
            except ValueError: print("Please enter a whole number.")
        elif c=="2": print("Inorder:",tree.inorder())
        elif c=="3": print("Preorder:",tree.preorder())
        elif c=="4": print("Postorder:",tree.postorder())
        else: print("Invalid choice.")

def main():
    actions={"1":search_demo,"2":sort_demo,"3":stack_demo,"4":queue_demo,"5":linked_list_demo,"6":bst_demo}
    while True:
        print("\n========== DATA STRUCTURES & ALGORITHMS TOOLKIT ==========\n1. Searching algorithms\n2. Sorting algorithms\n3. Stack (LIFO)\n4. Queue (FIFO)\n5. Singly linked list\n6. Binary search tree\n0. Exit\n==========================================================")
        c=input("Enter your choice: ").strip()
        if c=="0": print("Thanks for exploring the DSA Toolkit."); return
        if c not in actions: print("Invalid choice. Please select 0 to 6."); continue
        actions[c]()

if __name__=="__main__":
    try: main()
    except (EOFError,KeyboardInterrupt): print("\nApplication closed.")
