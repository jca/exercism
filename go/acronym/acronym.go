// Package acronym prepares acronyms of phrases
package acronym

import (
	"bytes"
	"strings"
	"unicode"
)

// Abbreviate returns
// a string containing the acronym of the sentence passed in
func Abbreviate(s string) string {
	var p string
	var letters bytes.Buffer

	for _, ch := range s {
		previousIsSpace := p == "" || strings.ContainsAny(p, " \t_")
		currentIsLetter := unicode.IsLetter(ch)
		if previousIsSpace && currentIsLetter {
			letters = append(letters, ch)
		}
		p = ch
	}

	return strings.Join(letters, "")
}
