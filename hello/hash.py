class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        hashValue = hash(key)
        hashIndex = hashValue % len(self.items)
        self.items[hashIndex] = value
        return

    def get(self, key):
        hashValue = hash(key)
        hashIndex = hashValue % len(self.items)

        return self.items[hashIndex]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!