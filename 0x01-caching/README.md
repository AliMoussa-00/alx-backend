# Caching System Overview

[tasks](https://drive.google.com/file/d/1pQsfOlBJdnzK6N8hjuwCTjy56zp9gJXz/view?usp=drive_link)

---

## What is a Caching System?

A caching system is like a storage space that keeps frequently used information nearby for quick access. It helps speed up data retrieval by storing commonly accessed data in a cache.

## Key Caching Algorithms:

- **FIFO** (First In, First Out): The first item added to the cache is the first one to be removed.
- **LIFO** (Last In, First Out): The last item added to the cache is the first one to be removed.
- **LRU** (Least Recently Used): Replaces the least recently used items from the cache when it's full.
- **MRU** (Most Recently Used): Replaces the most recently used items from the cache when it's full.
- **LFU** (Least Frequently Used): Removes the least frequently accessed items from the cache when it's full.

## Purpose of a Caching System:

The main purpose of a caching system is to speed up data retrieval. By storing frequently accessed data in a cache, it reduces the time it takes to fetch that data from its original source.

## Limits of a Caching System:

Caching systems have limitations such as size constraints, eviction policies, and cache coherence. These limits can impact the efficiency and effectiveness of the caching system.
