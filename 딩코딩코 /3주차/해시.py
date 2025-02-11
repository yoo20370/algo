class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):

        result = None 
        hash_code = hash(key)
        hash_index = hash_code % len(self.items)
        if self.items[hash_index] != None :
            result = self.items[hash_index]

        self.items[hash_index] = value
        return result

    def get(self, key):
        hash_code = hash(key)
        hash_index = hash_code % len(self.items)
    
        return self.items[hash_index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        hash_code = hash(key)
        hash_index = hash_code % len(self.items)
        linkedTuple = self.items[hash_index]

        linkedTuple.add(key,value)
        return None

    def get(self, key):
        hash_code = hash(key)
        hash_index = hash_code % len(self.items)
        linkedTuple = self.items[hash_index]
        
        return linkedTuple.get(key)