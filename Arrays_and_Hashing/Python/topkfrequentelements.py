from collections import defaultdict
import heapq


def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    freq_map = defaultdict(int)
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    heap = []

    for key, value in freq_map.items():
        if (len(heap) == k):
            heapq.heappushpop(heap, (value, key))
        else:
            heapq.heappush(heap, (value, key))

    out = []
    for i in range (k):
        out.append(heap[i][1])
    return out
        
        


print(topKFrequent([1,1,1,2,2,3], 2))