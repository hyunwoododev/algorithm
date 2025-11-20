package heap

func kClosest(points [][]int, k int) [][]int {
	minHeap := priorityqueue.NewWith(func(a, b interface{}) int {
		distA := a.([]int)[0]
		distB := b.([]int)[0]
		return distA - distB
	})

	for _, point := range points {
		x, y := point[0], point[1]
		dist := x*x + y*y
		minHeap.Enqueue([]int{dist, x, y})
	}

	res := [][]int{}
	for i := 0; i < k; i++ {
		item, _ := minHeap.Dequeue()
		point := item.([]int)
		res = append(res, []int{point[1], point[2]})
	}

	return res
}
