package arrayshashing

// https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	// use map[int]struct{} for O(1) membership check with zero allocation
	set := make(map[int]struct{}, len(nums))
	for _, n := range nums {
		set[n] = struct{}{}
	}

	longest := 0
	for n := range set {
		// only start counting from sequence "heads"
		if _, hasPrev := set[n-1]; hasPrev {
			continue
		}

		length := 1
		for next := n + 1; ; next++ {
			if _, ok := set[next]; !ok {
				break
			}
			length++
		}
		if length > longest {
			longest = length
		}
	}
	return longest
}
