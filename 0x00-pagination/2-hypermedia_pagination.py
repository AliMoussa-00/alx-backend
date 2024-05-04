#!/usr/bin/env python3
'''Simple pagination'''

import csv
import math
from typing import Dict, List, Tuple


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
        and return the appropriate dataset (the correct list of rows).
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''returns a dictionary containing the metadata'''
        data = self.get_page(page, page_size)
        data_len = len(self.__dataset)
        start_idx, end_idx = index_range(page, page_size)
        next_page = page + 1 if end_idx + page_size < data_len else None
        prev_page = page - 1 if start_idx - page_size >= 0 else None
        total_pages = math.ceil(data_len / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
