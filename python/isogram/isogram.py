def is_isogram(string):
    cleaned_string = string.lower().replace(' ', '').replace('-', '')
    return len(set(cleaned_string)) == len(cleaned_string)
