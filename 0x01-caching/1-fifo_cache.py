#!/usr/bin/python3
'''FIFO caching'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''defining the FIFOCache class'''

    def __init__(self):
        '''initializing the instance'''
        super().__init__()

    def put(self, key, item):
        '''add element to cache according to FIFO algorithm'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # delete the first key of the cache
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')

            self.cache_data[key] = item

    def get(self, key):
        '''get an element from cache'''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
