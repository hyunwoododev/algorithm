package heap

func leastInterval(tasks []byte, n int) int {
	count := make(map[byte]int)
	for _, task := range tasks {
		count[task]++
	}

	maxHeap := priorityqueue.NewWith(func(a, b interface{}) int {
		return b.(int) - a.(int)
	})
	for _, cnt := range count {
		maxHeap.Enqueue(cnt)
	}

	time := 0
	q := make([][2]int, 0)

	for maxHeap.Size() > 0 || len(q) > 0 {
		time++

		if maxHeap.Size() == 0 {
			time = q[0][1]
		} else {
			cnt, _ := maxHeap.Dequeue()
			cnt = cnt.(int) - 1
			if cnt.(int) > 0 {
				q = append(q, [2]int{cnt.(int), time + n})
			}
		}

		if len(q) > 0 && q[0][1] == time {
			maxHeap.Enqueue(q[0][0])
			q = q[1:]
		}
	}

	return time
}
