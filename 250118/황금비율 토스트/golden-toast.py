n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Write your code here!

class Node:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class DoubleLinkedList:
    def __init__(self):
        self.END = Node(-1) # 구현 편의 위한 dummmy값
        self.head = self.END
        self.tail = self.END

    def push_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        self.head.prev = new_node
        self.head = new_node
    
    def push_back(self,new_data):
        if self.begin() == self.end(): # 리스트가 비어있다면 맨 앞에 넣는 것과 똑같다
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self,node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node

    def insert(self,node,new_data):
        if node == self.begin():
            self.push_front(new_data)
        
        elif node == self.end():
            self.push_back(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    def print_all_nodes(self):
        it = self.begin()
        while it != self.end():
            print(it.data,end="")
            it = it.next


    
li = DoubleLinkedList()
# s를 li에 넣는다
for i in s:
    li.push_back(i) 

it = li.end()
for cmd in commands:
    if cmd[0] == 'L':
        if it == li.begin():
            continue
        else:
            it = it.prev
    if cmd[0] == 'R':
        if it == li.end():
            continue
        else:
            it = it.next
    if cmd[0] == 'D':
        if it == li.end():
            continue
        else:
           it = li.erase(it)
    if cmd[0] == 'P':
        li.insert(it,cmd[1])
    # li.print_all_nodes()
    # print('\n')

li.print_all_nodes()



