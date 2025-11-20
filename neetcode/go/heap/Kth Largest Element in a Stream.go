package heap

type KthLargest struct {
	minHeap *priorityqueu.Queue
	k       int
}

func Constructor(k int, nums []int) KthLargest {
	minHeap := priorityqueue.NewWith(utils.IntComparator)
	for _, num := range nums {
		minHeap.Enqueue(num)
	}
	for minHeap.Size() > k {
		minHeap.Dequeue()
	}
	return KthLargest{minHeap: minHeap, k: k}
}

func (this *KthLargest) Add(val int) int {
	this.minHeap.Enqueue(val)
	if this.minHeap.Size() > this.k {
		this.minHeap.Dequeue()
	}
	top, _ := this.minHeap.Peek()
	return top.(int)
}
