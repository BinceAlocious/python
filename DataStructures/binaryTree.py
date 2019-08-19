class node:
    def __init__(self,value=None):  #only if no value passed value assigned as None
        self.value=value
        self.left_child=None
        self.right_child=None
class binary_search_tree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if(self.root==None):
            self.root=node(value)
        else:
            self._insert(value,self.root)    #underscore insert To create private methods(Can't be acessed outside class)

    def _insert(self,value,cur_node):        #Private method
        if(value<cur_node.value):
            if(cur_node.left_child==None):
                cur_node.left_child=node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif(value>cur_node.value):
            if(cur_node.right_child==None):
                cur_node.right_child=node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value Already in Tree")
    def print_tree(self):
        if(self.root!=None):
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if(cur_node!=None):
            print(str(cur_node.value))
            self._print_tree(cur_node.left_child)
            self._print_tree(cur_node.right_child)
    def search(self,val):
        if(self.root!=None):
            return self._search(val,self.root)
        else:
            return False
    def _search(self,val,cur_node):
        if(cur_node.value==val):
            return True
        elif(cur_node.value>val and cur_node.left_child!=None):
            return self._search(val,cur_node.left_child)
        elif(cur_node.value<val and cur_node.right_child!=None):
            return self._search(val,cur_node.right_child)
        else:
            return False
op=int(input("Enter Option: 1.Add 2.Display 3.Search 4.Exit"))
obj=binary_search_tree()
while(op!=4):
    if(op==1):
        val=int(input("Enter Value: "))
        obj.insert(val)
        op = int(input("Enter Option: 1.Add 2.Display 3.Search 4.Exit"))
    elif(op==2):
        obj.print_tree()
        op = int(input("Enter Option: 1.Add 2.Display 3.Search 4.Exit"))
    elif(op==3):
        el=int(input("Enter Value To Search: "))
        bool=obj.search(el)
        print(bool)
        op = int(input("Enter Option: 1.Add 2.Display 3.Search 4.Exit"))
    elif(op==4):
        break
    else:
        print("Invalid Input")
        op = int(input("Enter Option: 1.Add 2.Display 3.Search 4.Exit"))