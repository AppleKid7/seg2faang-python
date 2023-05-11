
class HashMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self):
        self.store = [[] * 16]
        self.size = 0

    def get(self, key):
        index = hash(key) % len(self.store)
        chain = self.store[index]
        for kv in chain:
            if kv.key == key:
                return kv.value
        return None

    def put(self, key, value):
        new_node = HashMapNode(key, value)
        index = hash(key) % len(self.store)
        list_at_index = self.store[index]
        already_existed = False
        for kv in list_at_index:
            if kv.key == key:
                kv.value = value
                already_existed = True
                break

        if not already_existed:
            list_at_index.append(new_node)
            self.size += 1

    def delete(self, key):
        index = hash(key) % len(self.store)
        list_at_index = self.store[index]
        for kv in list_at_index:
            if kv.key == key:
                list_at_index.remove(kv)
                self.size -= 1
                break

    def __len__(self):
        return self.size

def main():
    pass

if __name__ == '__main__':
    main()
