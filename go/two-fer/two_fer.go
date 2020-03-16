// Package twofer is an exercism solution
package twofer

import (
	"fmt"
)

// ShareWith is a string utility which returns
// a string containing "One for {name}, one for me"
func ShareWith(name string) string {
	if name == "" {
		return "One for you, one for me."
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
