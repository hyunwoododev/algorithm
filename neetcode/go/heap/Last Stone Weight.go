package heap

func lastStoneWeight(stones []int) int {
	pq := priorityqueue.NewWith(func(a, b interface{}) int {
		return a.(int) - b.(int)
	})

	for _, s := range stones {
		pq.Enqueue(-s)
	}

	for pq.Size() > 1 {
		first, _ := pq.Dequeue()
		second, _ := pq.Dequeue()
		if second.(int) > first.(int) {
			pq.Enqueue(first.(int) - second.(int))
		}
	}

	pq.Enqueue(0)
	result, _ := pq.Dequeue()
	return -result.(int)
}
