import sys
import heapq

def runningMedian(nums):
    minHeap = []
    maxHeap = []
    output = []
    median = 0
    for i in nums:
        if i < median:
            heapq.heappush(minHeap, i)
            heapq._heapify_max(minHeap)
        else:
            heapq.heappush(maxHeap, i)
        if len(minHeap) > len(maxHeap)+1:
            heapq.heappush(maxHeap, heapq.heappop(minHeap))
            heapq._heapify_max(minHeap)
        elif len(maxHeap) > len(minHeap)+1:
            heapq.heappush(minHeap, heapq.heappop(maxHeap))
            heapq._heapify_max(minHeap)
        if len(minHeap) == len(maxHeap):
            median = (minHeap[0] + maxHeap[0])/2
        else:
            median = (minHeap[0]) if len(minHeap) > len(maxHeap) else maxHeap[0]
        output.append(median)
    return output

if __name__ == '__main__':
    nums = [int(e) for e in sys.argv[1:]]
    output = runningMedian(nums)
    print(output)

