class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        '''Malumotlarni chop qilish'''
        if self.head is None:
            print("Ro'yxat bo'sh")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def push(self, new_data):
        '''Boshiga element qo'shish'''
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        '''Biror tugundan keyin element qo'shish'''
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

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

    def deleteNode(self, key):
        '''Listni qiymatini o'chirish'''
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"'{key}' qiymati ro'yxatda topilmadi")
            return

        prev.next = temp.next
        temp = None


llist = LinkedList()
llist.head = Node("Dushaba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")
llist.head.next = tuesday
tuesday.next = wednesday
llist.push("Yakshanba")
llist.insertAfter(llist.head.next, "Salom Dushanba")
# llist.append("Payshanba")
llist.deleteNode("Payshanba")
print(llist.printList())
