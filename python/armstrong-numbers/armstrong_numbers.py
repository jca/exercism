def is_armstrong(number):
    string = str(number)
    power = len(string)
    return sum(int(x)**power for x in string) == number
