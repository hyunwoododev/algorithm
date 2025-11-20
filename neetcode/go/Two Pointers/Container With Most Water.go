package twopointers

func maxArea(heights []int) int {
	l, r := 0, len(heights)-1
	res := 0

	for l < r {
		area := min(heights[l], heights[r]) * (r - l)
		if area > res {
			res = area
		}
		if heights[l] <= heights[r] {
			l++
		} else {
			r--
		}
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
