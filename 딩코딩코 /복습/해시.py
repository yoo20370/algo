class LinkedTuple :

    def __init__(self) :
        self.items = []

    def add(self, key, value) -> None :
        self.items.append((key,value))
    
    def get(self, key) :
        for k, v in self.items :
            if key == k :
                return v

class LinkedDict :

    def __init__(self) :
        self.items = []
        for i in range(8) :
            self.items.append(LinkedTuple())

    def put(self, key, value) -> None :
        hash_index = hash(key) % len(self.items)
        self.items[hash_index].add(key,value)
    
    def get(self, key) -> int :
        hash_index = hash(key) % len(self.items)
        return self.items[hash_index].put(key)


class Dict :

    def __init__(self) :
        self.items = [None] * 8

    def put(self, key, value) -> None :
        hash_index = hash(key) % len(self.items)
        self.items[hash_index] = value

    def get(self, key) -> int :
        hash_index = hash(key) % len(self.items)
        return self.items[hash_index]