#if !defined(DIFFERENCE_OF_SQUARES_H)
#define DIFFERENCE_OF_SQUARES_H
#include <cmath>

namespace difference_of_squares {

    unsigned square_of_sum(unsigned value) {
        return pow(value*(value+1)/2, 2);
    }

    unsigned sum_of_squares(unsigned value) {
        int sum = 0;
        for (unsigned i = 1; i <= value; i++) {
            sum += i*i;
        }
        return sum;
    }

    unsigned difference(unsigned value) {
        return square_of_sum(value) - sum_of_squares(value);
    }

}  // namespace difference_of_squares

#endif // DIFFERENCE_OF_SQUARES_H