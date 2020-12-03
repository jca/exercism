package matrix

import (
	"strings"
	"strconv"
	"errors"
)

type Matrix [][]int

func New(text string) (Matrix, error)  {
	lines := strings.Split(text, "\n")
	var columnCount int
	m := make(Matrix, len(lines))

	for i, line := range lines {
		parts := strings.Split(strings.TrimSpace(line), " ")
		m[i] = make([]int, len(parts))

		for j, c := range parts {
			if i == 0 {
				columnCount = len(parts)
			} else if columnCount != len(parts) {
				return nil, errors.New("Inconsistent column count!")
			}

			ci, err := strconv.Atoi(c)
			if (err != nil) {
				return nil, err
			}
			m[i][j] = ci
		}
	}

	return m, nil
}

func (m Matrix) Rows() [][]int {
	var clone [][]int
	if len(m) == 0 {
		return clone
	}
	clone = make([][]int, len(m))

	for i := 0; i<len(m); i++ {
		clone[i] = make([]int, len(m[0]))
		for j, _ := range m[0] {
			clone[i][j] = m[i][j]
		}
	}

	return clone
}

func (m Matrix) Cols() [][]int {
	var transpose [][]int
	if len(m) == 0 {
		return transpose
	}

	transpose = make([][]int, len(m[0]))

	for j := 0; j<len(m[0]); j++ {
		transpose[j] = make([]int, len(m))
		for i, _ := range m {
			transpose[j][i] = m[i][j]
		}
	}

	return transpose
}

func (m Matrix) Set(i, j, v int) bool {
	if i < 0 || j < 0 {
		return false
	}
	if i >= len(m) || j >= len(m[0]) {
		return false
	}

	m[i][j] = v
	return true
}