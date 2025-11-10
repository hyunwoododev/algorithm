// https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

package arrayshashing

import (
	"strconv"
	"strings"
)

type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	var sizes []string
	for _, str := range strs {
		sizes = append(sizes, strconv.Itoa(len(str)))
	}
	return strings.Join(sizes, ",") + "#" + strings.Join(strs, "")
}

func (s *Solution) Decode(encoded string) []string {
	if encoded == "" {
		return []string{}
	}
	parts := strings.SplitN(encoded, "#", 2)
	sizes := strings.Split(parts[0], ",")
	var res []string
	i := 0
	for _, sz := range sizes {
		if sz == "" {
			continue
		}
		length, _ := strconv.Atoi(sz)
		res = append(res, parts[1][i:i+length])
		i += length
	}
	return res
}
