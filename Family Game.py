class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self,key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def len_circularlinkedlist(self):
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count = count + 1
            cur = cur.next
        return count

    def final_func(self,cllistB):
        cur = self.head
        cur1 = cllistA.head

        if cllistA.len_circularlinkedlist() == 1:
            return cllistA.head.data

        while cllistA.len_circularlinkedlist() != 1:
            if cur.data == 'x':
                cur = cur.next
                cur1 = cur1.next
            elif cur.data == 'y':
                a = cur1.next
                cllistA.remove(cur1.data)
                cur = cur.next
                cur1 = a
        return cllistA.head.data


cllistA = CircularLinkedlist()
cllistB = CircularLinkedlist()

N = int(input())
s = input()
for i in range(N):
    cllistA.append(str(i+1))
