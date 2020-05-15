class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
            print(self.data)
            return self.data
        elif len(self.data) == self.capacity:
            print('current', self.current)
            self.data[self.current] = item
            print(self.data)

            if self.current == 4:
                self.current = 0
            else:
                self.current += 1
 

    def get(self):
        return self.data
