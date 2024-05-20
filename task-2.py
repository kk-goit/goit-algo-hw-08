import heapq

class MergeItem:
    """Item from list and list's idex"""

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __lt__(self, other):
        return self.val < other.val
    

def merge_k_lists(arrays):
    """Merge k arrays in one"""
    if not arrays:
        return []
    if len(arrays) == 1:
        return arrays[0]

    rezult = []
    mheap = []

    # initialize merge heap by first elemnts
    lenth = []
    posns = []
    idx = 0
    for a in arrays:
        lenth.append(len(a)) # length of current array
        posns.append(1) # position of the next item in current array
        if lenth[idx] > 0:
            heapq.heappush(mheap, MergeItem(a[0], idx)) # if list not empty - add first item to heap
        idx += 1

    # merged items from heap
    while len(mheap) > 0:
        min_item = heapq.heappop(mheap)
        rezult.append(min_item.val)
        if posns[min_item.idx] < lenth[min_item.idx]:
            heapq.heappush(mheap, MergeItem(arrays[min_item.idx][posns[min_item.idx]], min_item.idx))
            posns[min_item.idx] += 1
    
    return rezult

print(f"Merged arrays: {merge_k_lists([[1, 4, 5], [8], [], [1, 3, 4], [2, 6], [0]])}")
