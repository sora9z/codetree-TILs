N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Write your code here!
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self,new_data):
        # head 앞에 넣는다
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = self.head

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

        self.node_num +=1

    def push_back(self,new_data):
        # list끝에 넣는다
        new_node = Node(new_data)
        new_node.next = None
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.node_num +=1

    def pop_front(self):
        if self.head == None:
            print('List is empty')
        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else :
            temp = self.head
            temp.next.prev = None
            self.head = temp.next

            self.node_num -=1
            return temp.data

    def pop_back(self):
        if self.tail == None:
            print('List is empty')
        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num-=1
            return temp.data

    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data

    def size(self):
        return self.node_num
    
    def empty(self):
        return 1 if self.node_num == 0 else 0
            



double_linked_list = DoubleLinkedList()


for i in range(len(command)):  
    if command[i] == 'push_front':
        double_linked_list.push_front(A[i])
    if command[i] == 'push_back' :
        double_linked_list.push_back(A[i])
    if command[i] == 'pop_front':
        node = double_linked_list.pop_front()
        print(node)
    if command[i] == 'pop_back':
        node = double_linked_list.pop_back()
        print(node)
    if command[i] == 'front':
        print(double_linked_list.front())
    if command[i] == 'back':
        print(double_linked_list.back())
    if command[i] == 'size':
        print(double_linked_list.size())    
    if command[i] == 'empty':
        print(double_linked_list.empty())
        



    
        



            

