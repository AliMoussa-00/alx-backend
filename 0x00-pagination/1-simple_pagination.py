#!/usr/bin/env python3
'''Simple pagination'''

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    '''
    start_idx = (page - 1) * page_size
    end_idx = page * page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        A function find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        (i.e. the correct list of rows).
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        self.dataset()
        data_len = len(self.__dataset)
        start, end = index_range(page, page_size)

        if start >= data_len:
            return []
        if end >= data_len:
            end = data_len

        return self.__dataset[start:end]
