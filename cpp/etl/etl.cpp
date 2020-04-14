#include "./etl.h"

namespace etl {
    // Transform {points: [LETTER]} to {letter: points}
    NewMap transform(LegacyMap valueLetters)
    {
        NewMap letterValues;
        for (const auto &value : valueLetters)
        {
            for (auto letter : value.second)
            {
                letterValues[tolower(letter)] = value.first;
            }
        }

        return letterValues;
    }

} // namespace etl