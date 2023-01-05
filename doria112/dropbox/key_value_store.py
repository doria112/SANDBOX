from collections import defaultdict
class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.cid = 0 # current max used id
        self.key_to_ids = defaultdict(set) # key: set(id1, id2, ...)
        self.id_to_keys = defaultdict(set) # id: set(key1, key2, ...)
        self.changes = defaultdict(list) # id: [(k,v)]
        self.backups = defaultdict(list) # id: [(k,v)], may not need this
        self.open_ids = set()
        
    def _generate_transaction_id(self, incr):
        self.cid += incr
        return self.cid
    
    def start(self):
        id = self._generate_transaction_id(1)
        self.open_ids.add(id)
        return id
    
    def get(self, id, key):
        #num_locks = len(self.key_to_ids[key])
        if key not in self.key_to_ids or (len(self.key_to_ids[key]) == 1 and id in self.key_to_ids[key]):
            if key in self.store:
                self.key_to_ids[key].add(id)
                self.id_to_keys[id].add(key)
                return self.store[key]
            else:
                raise Exception("key doesn't exist")
        else: # conflict exists, roll back
            print(f"transaction {id} cannot be completed due to read conflict")
            self.rollback(id)
    
    def _remove_all_locks(self, id):
        for key in self.id_to_keys[id]:
            self.key_to_ids[key].remove(id)
            # todo remove key entirely if empty set
        del self.id_to_keys[id]
    
    def rollback(self, id):
        # remove id from open transactions
        # release all the locks
        # remove entries in changes and backups
        self.open_ids.remove(id)
        self._remove_all_locks(id)
        del self.changes[id]
        del self.backups[id]
    
    def set(self, id, key, value):
        #num_locks = len(self.key_to_ids[key])
        if key not in self.key_to_ids or (len(self.key_to_ids[key]) == 1 and id in self.key_to_ids[key]):
            self.changes[id].append((key, value))
            if key in self.store:
                self.backups[id].append((key, self.store[key]))
            else:
                self.backups[id].append((key, None))
        else:
            print(f"transaction {id} cannot be completed due to write conflict")
            self.rollback(id)
    
    def delete(self, id, key):
        num_locks = len(self.key_to_ids[key])
        if num_locks == 0 or (num_locks == 1 and id in self.key_to_ids[key]):
            del self.store[key]
        else:
            print(f"transaction {id} cannot be completed due to delete conflict")
            self.roll_back(id)
    
    def commit(self, id):
        if id in self.open_ids:
            self.open_ids.remove(id)
            # updates the main store
            for k,v in self.changes[id]:
                self.store[k] = v
            # release all locks
            self._remove_all_locks(id)
            # remvoe from open ids 
        else:
            print(f"transaction {id} is not open, cannot be committed")

kvs = KeyValueStore()
t1 = kvs.start()
print(kvs.set(t1, "a", 3))
kvs.commit(t1)
t2 = kvs.start()
print(kvs.get(t2, "a"))
kvs.delete(t2, "a")
#print(kvs.get(t2, "a"))
kvs.set(t2, "a", 8)
t3 = kvs.start()
print(kvs.set(t3, "b", 5))
kvs.set(t3, "a", 9)
kvs.commit(t3)
print(kvs.get(t2, "b"))
