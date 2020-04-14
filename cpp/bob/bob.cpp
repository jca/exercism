#include "bob.h"

#include <string>
#include <stdexcept>

namespace bob {
    bool is_question(std::string text) {
        for (int i=text.length()-1; i>=0; i--) {
            if (::isblank(text[i]) || ::isspace(text[i])) {
                continue;
            }
            if ('?' == text[i]) {
                return true;
            } else {
                break;
            }
        }
        return false;
    }

    bool is_upper_text(std::string text) {
        bool hasAlpha = false;
        for(const auto c: text) {
            if (::isalpha(c)) {
                if (::islower(c)) {
                    return false;
                }
                hasAlpha = true;
            }
        }
        return hasAlpha;
    }

    bool is_empty_text(std::string text) {
        for(const auto c: text) {
            if (!::isblank(c) && !::isspace(c)) {
                return false;
            }
        }
        return true;
    }

    std::string hey(std::string salute) {
        if (is_empty_text(salute)) {
            return "Fine. Be that way!";
        }
        if (is_question(salute)) {
            if (is_upper_text(salute)) {
                return "Calm down, I know what I'm doing!";
            }
            return "Sure.";
        }
        if (is_upper_text(salute)) {
            return "Whoa, chill out!";
        }

        return "Whatever.";
    }
}  // namespace bob
