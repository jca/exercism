#if !defined(ETL_H)
#define ETL_H

#include <map>
#include <tuple> // std::tie
#include <vector>
#include <utility> // std::pair

namespace etl {
    using NewMap = std::map<char, int>;
    using LegacyMap = std::map<int, std::vector<char>>;

    // Transform {points: [LETTER]} to {letter: points}
    NewMap transform(LegacyMap valueLetters);

}  // namespace etl

#endif // ETL_H