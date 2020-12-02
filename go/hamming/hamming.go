package hamming

import "errors"

func Distance(a, b string) (int, error) {
	// Transform first to an array of runes to deal with multi-byte characters
	ra := []rune(a)
	rb := []rune(b)

	if len(ra) != len(rb) {
		return -1, errors.New("Both strings must have equal lengths")
	}

 	distance := 0
	for i := range ra {
		if ra[i] != rb[i] {
			distance += 1
		}
	}
	return distance, nil
}
