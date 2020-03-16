#include "hamming.h"
#include <string>

using namespace std;

namespace hamming {
    unsigned int compute(string a, string b) {
        if (a.size() != b.size()) {
            throw domain_error("Strand lengths must be equal!");
        }

        unsigned int distance = 0;
        for (unsigned int i = 0; i < a.size(); i++) {
            distance += a[i] != b[i];
        }

        return distance;
    }
}  // namespace hamming
