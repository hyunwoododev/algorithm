package heap

type Twitter struct {
	count     int
	tweetMap  map[int][][]int      // userId -> list of [count, tweetId]
	followMap map[int]map[int]bool // userId -> set of followeeId
}

func Constructor() Twitter {
	return Twitter{
		count:     0,
		tweetMap:  make(map[int][][]int),
		followMap: make(map[int]map[int]bool),
	}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
	if this.tweetMap[userId] == nil {
		this.tweetMap[userId] = make([][]int, 0)
	}
	this.tweetMap[userId] = append(this.tweetMap[userId], []int{this.count, tweetId})
	this.count--
}

func (this *Twitter) GetNewsFeed(userId int) []int {
	res := make([]int, 0)

	minHeap := priorityqueue.NewWith(func(a, b interface{}) int {
		return a.([]int)[0] - b.([]int)[0]
	})

	if this.followMap[userId] == nil {
		this.followMap[userId] = make(map[int]bool)
	}
	this.followMap[userId][userId] = true

	for followeeId := range this.followMap[userId] {
		tweets := this.tweetMap[followeeId]
		if len(tweets) > 0 {
			index := len(tweets) - 1
			count, tweetId := tweets[index][0], tweets[index][1]
			minHeap.Enqueue([]int{count, tweetId, followeeId, index - 1})
		}
	}

	for minHeap.Size() > 0 && len(res) < 10 {
		item, _ := minHeap.Dequeue()
		curr := item.([]int)
		count, tweetId, followeeId, index := curr[0], curr[1], curr[2], curr[3]

		res = append(res, tweetId)

		if index >= 0 {
			tweets := this.tweetMap[followeeId]
			count, tweetId = tweets[index][0], tweets[index][1]
			minHeap.Enqueue([]int{count, tweetId, followeeId, index - 1})
		}
	}

	return res
}

func (this *Twitter) Follow(followerId int, followeeId int) {
	if this.followMap[followerId] == nil {
		this.followMap[followerId] = make(map[int]bool)
	}
	this.followMap[followerId][followeeId] = true
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
	if this.followMap[followerId] != nil {
		delete(this.followMap[followerId], followeeId)
	}
}
