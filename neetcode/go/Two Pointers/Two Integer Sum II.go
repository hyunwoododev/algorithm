package twopointers

// https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

func twoSum(numbers []int, target int) []int {
	l, r := 0, len(numbers)-1

	for l < r {
		curSum := numbers[l] + numbers[r]
		if curSum > target {
			r--
		} else if curSum < target {
			l++
		} else {
			return []int{l + 1, r + 1}
		}
	}
	return []int{}
}
