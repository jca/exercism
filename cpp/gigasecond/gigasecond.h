#if !defined(GIGASECOND_H)
#define GIGASECOND_H

#include "boost/date_time/posix_time/posix_time.hpp"

using namespace boost::posix_time;

int const GIGASECOND = 1'000'000'000;

namespace gigasecond {
    ptime advance(ptime in) {
        return in + seconds(GIGASECOND);
    }
}  // namespace gigasecond

#endif // GIGASECOND_H