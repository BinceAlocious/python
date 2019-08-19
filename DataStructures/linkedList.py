class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=Node()
    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while(cur.next!=None):
            total+=1
            cur=cur.next
        return total
    def search(self,val):
        cur_node=self.head
        flag=0
        while(cur_node.next!=None):
            cur_node=cur_node.next
            if(cur_node.data==val):
                flag=1
                break
        if(flag==1):
            return True
        else:
            return False

    def display(self):
        elems=[]
        cur_node=self.head
        while(cur_node.next!=None):
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
obj=Linked_list()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj.length())
obj.display()
print(obj.search(20))
print(obj.search(40))