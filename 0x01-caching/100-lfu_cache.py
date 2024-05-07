#!/usr/bin/python3
'''LFU (Least Frequently Used) Caching'''


from collections import defaultdict
from typing import Any
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''Defining the LFUCache class'''

    def __init__(self):
        '''initializing the instance'''
        super().__init__()
        # this list will store the keys and how many they are used
        # {key: counter}
        self.queue = {}

    def put(self, key, item):
        '''add element to cache according to LFU algorithm'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                    key not in self.cache_data:
                # delete the least frequent key
                lfu_counter = min(list(self.queue.values()))
                lfu_key = self._get_key_by_value(self.queue, lfu_counter)
                if lfu_key:
                    del self.queue[lfu_key]
                    del self.cache_data[lfu_key]
                    print(f'DISCARD: {lfu_key}')

            counter = self.queue.get(key, 0) + 1
            self.queue[key] = counter
            self.cache_data[key] = item

    def get(self, key):
        '''get an element from cache'''
        if key and key in self.cache_data:
            # increase the counter for a used key
            counter = self.queue.get(key) + 1
            self.queue[key] = counter

            return self.cache_data[key]
        return None

    def _get_key_by_value(self, dictionary: dict, value: int) -> Any:
        '''return the key of a value in a dict'''

        for k, v in dictionary.items():
            if v == value:
                return k
        return None
