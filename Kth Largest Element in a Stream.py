import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.pool = nums
        self.k = k

        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)


    def add(self, val: int) -> int:  
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            heapq.heappushpop(self.pool, val)
        return self.pool[0]
    
obj = KthLargest(3, [1, 1])
obj.add(1)
obj.add(1)
obj.add(3)
obj.add(3)
obj.add(3)
obj.add(4)
obj.add(4)
obj.add(4)





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)