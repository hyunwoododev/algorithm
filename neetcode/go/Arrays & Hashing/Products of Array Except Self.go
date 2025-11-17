// https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

package arrayshashing

func productExceptSelf(nums []int) []int {
    leftRes := make([]int, len(nums))
    rightRes := make([]int, len(nums))

    for i := 0; i < len(nums); i++ {
        if i == 0 {
            leftRes[i] = 1
        } else {
            leftRes[i] = nums[i-1] * leftRes[i-1]
        }
    }

    for j := len(nums)-1; j >= 0; j-- {
        if j == len(nums)-1 {
            rightRes[j] = 1
        } else {
            rightRes[j] = nums[j+1] * rightRes[j+1]
        }
    }

    // 🔥 여기만 수정하면 됨
    res := make([]int, len(nums))
    for i := 0; i < len(nums); i++ {
        res[i] = leftRes[i] * rightRes[i]
    }

    return res
}