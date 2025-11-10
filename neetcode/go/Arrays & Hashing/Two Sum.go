// https://neetcode.io/problems/two-integer-sum?list=neetcode150

package arrayshashing

func twoSum(nums []int, target int) []int {
	indices := make(map[int]int)

	for i, n := range nums {
		indices[n] = i
	}

	for i, n := range nums {
		diff := target - n
		if j, found := indices[diff]; found && j != i {
			return []int{i, j}
		}
	}
	return []int{}
}
