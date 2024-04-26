
class Queue:
    def __init__(self,lst=[]):
        self.q=lst.copy()

    def push_back(self, x):
        self.q.append(x)

    def empty(self):
        return len(self.q)==0

    def pop_front(self):
        if self.empty():
            raise ValueError("Lista jest pusta!")
        return self.q.pop(0)

    def front(self):
        if self.empty():
            raise ValueError("Lista jest pusta!")
        return self.q[0]

if __name__ == "__main__":
    a=Queue()
    a.push_back(1)
    print(a.pop_front())
    print(a.q)
    #print(a.pop_front())
    b=Queue([0,2,3,4])
    print(b.front())
    print(b.q)
    a.push_back(b.pop_front())
    print(b.q)
    print(a.q)
