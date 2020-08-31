import datetime
class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.time = datetime.datetime.now().timestamp()


    def append(self, item):
        new_item = {"item_key":item, "timestamp" : datetime.datetime.now().timestamp()}
        
        if len(self.storage) < self.capacity:
            self.storage.append(new_item)
        else:
            oldest = self.storage[0]
            for item in self.storage:
                if item["timestamp"] < oldest["timestamp"]:
                    oldest = item
            index_of_oldest = self.storage.index(oldest)
            self.storage.pop(index_of_oldest)
            self.storage.insert(index_of_oldest,new_item) 
    def get(self):
        item_list = []
        for i in self.storage:
            item_list.append(i["item_key"])
        print(item_list)
        return item_list

ne = RingBuffer(3)
ne.append(3)
ne.append('s')
ne.append('g')
ne.append(6)
ne.get()