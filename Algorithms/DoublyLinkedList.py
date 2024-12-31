class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        '''Ro'yxatni chop etish'''
        if self.head is None:
            print("Ro'yxat bo'sh")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, new_data):
        '''Ro'yxat boshiga element qo'shish'''
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, new_data):
        '''Oxiriga element qo'shish'''
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insertAfter(self, prev_node, new_data):
        '''Biror tugundan keyin element qo'shish'''
        if prev_node is None:
            print("Oldingi tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next is not None:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def deleteNode(self, key):
        '''Qiymatga ko'ra tugunni o'chirish'''
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev

                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next
        print(f"'{key}' ro'yxatda topilmadi")

    def reverse(self):
        '''Ro'yxatni teskari o'girish'''
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev


Llist = DoublyLinkedList()
Llist.head = Node("1-knot")
knot2 = Node("2-knot")
knot3 = Node("3-knot")
Llist.head.next = knot2
knot2.prev = Llist.head
knot2.next = knot3
knot3.prev = knot2
Llist.push("0-knot")
Llist.insertAfter(knot2.next, "4-knot")
Llist.deleteNode("0-knot")
Llist.printList()
Llist.reverse()
Llist.printList()