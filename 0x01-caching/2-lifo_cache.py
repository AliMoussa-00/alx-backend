#!/usr/bin/python3
'''LIFO Caching'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Defining the LIFOCache class'''

    def __init__(self):
        '''initializing the instance'''
        self.queue = []
        super().__init__()

    def put(self, key, item):
        '''add element to cache according to LIFO algorithm'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                    key not in self.cache_data:
                # delete the first key of the cache
                last_key = self.queue.pop()
                del self.cache_data[last_key]

                print(f'DISCARD: {last_key}')

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''get an element from cache'''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
