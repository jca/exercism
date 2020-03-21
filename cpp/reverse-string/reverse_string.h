#include <string>

namespace reverse_string {
    std::string reverse_string(std::string text) {
        return std::string(text.rbegin(), text.rend());
    }
}  // namespace reverse_string
