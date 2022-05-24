class Heap_Item:

    def __init__(self, k, v):
        self.key = k
        self.value = v


    def __repr__(self):
        return "({},{})".format(self.key, self.value)



class Min_Heap:
    def __init__(self):
        self.heap = []
        self.index = {}


    def key(self, v):
        return self.heap[self.index[v]].key


    def left(self, i):
        return 2*i+1


    def right(self, i):
        return 2*(i+1)


    def parent(self, i):
        return (i-1)//2


    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        min = i

        if l < len(self) and self.heap[l].key < self.heap[min].key:
            min = l
        if r < len(self) and self.heap[r].key < self.heap[min].key:
            min = r

        if min != i:
            self.swap(i, min)
            self.min_heapify(min)


    def extract_min(self):
        if not self:
            return None
        self.swap(0, len(self)-1)
        min = self.heap.pop()
        del self.index[min.value]
        self.min_heapify(0)
        return (min.key, min.value)


    def insert(self, k, v):
        self.heap.append(Heap_Item(k,v))
        self.index[v] = len(self)-1
        self.decrease_key(v,k)


    def decrease_key(self, v, k):
        # NOTE: assumes that value v is present in the heap 
        # NOTE: assumes that the key of the element holding
        #       value v is >= k.
        i = self.index[v]
        item = self.heap[i]
        item.key = k

        p = self.parent(i)
        while i > 0 and k < self.heap[p].key:
            self.heap[i] = self.heap[p]
            self.index[self.heap[p].value] = i
            i, p = p, self.parent(p)

        self.heap[i] = item
        self.index[item.value] = i


    def swap(self, i, j):
        self.index[self.heap[i].value], self.index[self.heap[j].value] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def __len__(self):
        return len(self.heap)


    def __bool__(self):
        return len(self.heap) > 0


    def __contains__(self, v):
        return v in self.index

