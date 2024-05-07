#!/usr/bin/python3
'''LRU (Least Recently Used) Caching'''


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Defining the LRUCache class'''

    def __init__(self):
        '''initializing the instance'''
        super().__init__()
        # this list will store the keys sorted from least to most used
        self.queue = []

    def put(self, key, item):
        '''add element to cache according to LRU algorithm'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # delete the least used key, which is at index 0 of queue
                least_used = self.queue.pop(0)

                if key not in self.cache_data:
                    del self.cache_data[least_used]
                    print(f'DISCARD: {least_used}')

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''get an element from cache'''
        if key and key in self.cache_data:
            # change the sorting of the used key
            # by moving it from its index to the end of list
            del self.queue[self.queue.index(key)]
            self.queue.append(key)

            return self.cache_data[key]
        return None
