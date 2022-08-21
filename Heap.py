#### Max heap with Priority Queue

class MaxHeap:
    def __init__(self):
        self._heap = []
    
    def __parent(self, index):
        return (index-1 )//2 
    
    def __leftChild(self,index):
        return (index * 2) + 1
    
    def __rightChild(self,index):
        return (index * 2) + 2


    def size(self):
        return len(self._heap)

    def isEmpty(self):
        if self.size == 0 :
            return True
        else:
            return False
    
    def seek(self):
        return self._heap[0]

    def push(self,value):
        self._heap.append(value)
        i = self.size()-1
        while i > 0 and i< self.__parent(i):
            p = self.__parent(i)
            self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
            i = p
        print(self._heap)






h1 = MaxHeap()
# print(h1.__parent())
h1.push(50)
h1.push(25)
h1.push(45)
h1.push(35)
h1.push(10)
h1.push(15)
h1.push(20)
h1.push(40)
h1.push(75)