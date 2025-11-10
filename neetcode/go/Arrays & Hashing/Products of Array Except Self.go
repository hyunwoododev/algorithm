// https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

func productExceptSelf(nums []int) []int {
    n := len(nums)
    res := make([]int, n)
    pref := make([]int, n)
    suff := make([]int, n)

    pref[0], suff[n-1] = 1, 1
    for i := 1; i < n; i++ {
        pref[i] = nums[i-1] * pref[i-1]
    }
    for i := n - 2; i >= 0; i-- {
        suff[i] = nums[i+1] * suff[i+1]
    }
    for i := 0; i < n; i++ {
        res[i] = pref[i] * suff[i]
    }
    return res
}