class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        '''Ro'yxatni chop etish'''
        if self.head is None:
            print("Ro'yxat bo'sh")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def push(self, new_data):
        '''Ro'yxat boshiga element qo'shish'''
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def append(self, new_data):
        '''Oxiriga element qo'shish'''
        new_node = Node(new_data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insertAfter(self, prev_node, new_data):
        '''Biror tugundan keyin element qo'shish'''
        if prev_node is None:
            print("Oldingi tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, key):
        '''Qiymatga ko'ra tugunni o'chirish'''
        if self.head is None:
            print("Ro'yxat bo'sh")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == key:
                if temp == self.head:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        last.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = temp.next
                temp = None
                return
            prev = temp
            temp = temp.next
            if temp == self.head:
                break
        print(f"'{key}' ro'yxatda topilmadi")


cllist = CircularLinkedList()
cllist.push("2-knot")
cllist.push("0-knot")
cllist.append("4-knot")
cllist.insertAfter(cllist.head, "1-knot")
cllist.deleteNode("4-knot")
cllist.printList()
