class HashMap:
    TOMBSTONE = object()

    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        while self.hashmap[index] and self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] != key:
            index = (index + 1) % len(self.hashmap)
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        checked = 0
        while self.hashmap[index] and checked < len(self.hashmap):
            if self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            index = (index + 1) % len(self.hashmap)
            checked += 1
        raise Exception("sorry, key not found")
    
    def delete(self, key):
        index = self.key_to_index(key)
        checked = 0
        while self.hashmap[index] and checked < len(self.hashmap):
            if self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] == key:
                self.hashmap[index] = self.TOMBSTONE
                return
            index = (index + 1) % len(self.hashmap)
            checked += 1
        raise Exception("sorry, key not found")

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
        if self.current_load() < 0.05:
            return
        old_hashmap = self.hashmap
        new_hashmap = HashMap((len(old_hashmap)*10))
        for item in old_hashmap:
            if item is not None:
                key, value = item
                new_hashmap.insert(key, value)
        self.hashmap = new_hashmap.hashmap

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        return sum(1 for item in self.hashmap if item is not None) / len(self.hashmap)

    def key_to_index(self, key) -> int:
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v is not None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
