package heap

func findKthLargest(nums []int, k int) int {
	minHeap := priorityqueue.NewWith(utils.IntComparator)

	for _, num := range nums {
		minHeap.Enqueue(num)
		if minHeap.Size() > k {
			minHeap.Dequeue()
		}
	}

	val, _ := minHeap.Peek()
	return val.(int)
}
