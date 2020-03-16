// Package gigasecond adds a gigasecond to a time
package gigasecond

// import path for the time package from the standard library
import "time"

const gigasecond = 1e9 * time.Second

// AddGigasecond adds a gigasecond to a time
// returns a time a gigasecond later
func AddGigasecond(t time.Time) time.Time {
	return t.Add(gigasecond)
}
