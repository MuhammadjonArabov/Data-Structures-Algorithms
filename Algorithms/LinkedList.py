class Node:
    def __init__(self, data):
        self.data = data,
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        '''Malumotlarni chop qilish'''
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        '''Boshiga elemnt qo'shish'''
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def insertAfter(self, prev_node, new_data):
        '''Birir tugundan keyin element qo'shihs'''
        if prev_node is Node:
            print("Tugun mavjud emas")
        new_data = Node(new_data)
        new_data.next = prev_node.next
        prev_node.next = new_data

    def append(self, new_data):
        '''Oxriga element qo'shish'''
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data

    def deleteNode(self, key):
        '''Listni qiymatini o'chirish'''
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return

        prev.next = temp.next
        temp = None


llist = LinkedList()
llist.head = Node("Dushaba")
tusdey = Node("Seshanba")
wansdey = Node("Chorshanba")
llist.head.next = tusdey
tusdey.next = wansdey
llist.push("Yakshanba")
llist.insertAfter(llist.head.next, "Salom Dushanba")
#llist.append("Payshanba")
llist.deleteNode("Payshanba")
print(llist.printList())
