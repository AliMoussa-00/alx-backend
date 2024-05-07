#!/usr/bin/python3
'''Basic dictionary'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''defining the BasicCache'''

    def __init__(self):
        '''initialize the instance'''

        super().__init__()

    def put(self, key, item):
        '''add an item to the cache'''

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''get an item from the cache'''

        if key and key in self.cache_data:
            return self.cache_data.get(key)

        return None
