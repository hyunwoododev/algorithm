// https://neetcode.io/problems/is-anagram?list=neetcode150
package arrayshashing

func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false 
    }

    countS := make(map[rune]int, len(s))
    countT := make(map[rune]int, len(t))

    for index, ch := range s{
        countS[ch]++
        countT[rune(t[index])]++
    }

    for k, v := range countS{
        if ch, found := countT[k]; found && ch == v {
            continue
        }
        return false
    }
    return true
}
