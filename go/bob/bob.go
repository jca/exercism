// Package bob is a lackadaisical teenbot
package bob

import (
	"strings"
	"unicode"
)

const answerYellQuestion = "Calm down, I know what I'm doing!"
const answerQuestion = "Sure."
const answerYell = "Whoa, chill out!"
const answerNothing = "Fine. Be that way!"
const answerAnything = "Whatever."

// Hey is your typical teen and returns
// a boring answer
func Hey(remark string) string {
	remark = strings.Trim(remark, " \t\n\r")

	if isEmpty(remark) {
		return answerNothing
	}

	if isQuestion(remark) {
		if isYelled(remark) {
			return answerYellQuestion
		}
		return answerQuestion
	}

	if isYelled(remark) {
		return answerYell
	}

	return answerAnything
}

func isYelled(remark string) bool {
	return strings.IndexFunc(remark, unicode.IsLetter) != -1 && remark == strings.ToUpper(remark)
}

func isQuestion(remark string) bool {
	return remark[len(remark)-1:] == "?"
}

func isEmpty(remark string) bool {
	return strings.Trim(remark, " \t") == ""
}
