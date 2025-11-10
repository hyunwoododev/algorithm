package arrayshashing

// https://neetcode.io/problems/duplicate-integer?list=neetcode150

func hasDuplicate(nums []int) bool {
	set := make(map[int]struct{})
	for _, num := range nums {
		if _, found := set[num]; found {
			return true
		}
		set[num] = struct{}{}
	}
	return false
}
