// https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

package arrayshashing

func productExceptSelf(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	// 1) 왼쪽(접두) 곱 채우기: res[i] = nums[0..i-1]의 곱
	prefix := 1
	for i := 0; i < n; i++ {
		res[i] = prefix
		prefix *= nums[i]
	}

	// 2) 오른쪽(접미) 곱 곱해주기: res[i] *= nums[i+1..n-1]의 곱
	suffix := 1
	for i := n - 1; i >= 0; i-- {
		res[i] *= suffix
		suffix *= nums[i]
	}

	return res
}
