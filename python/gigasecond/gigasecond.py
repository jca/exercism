from datetime import timedelta

def add_gigasecond(birth_date, _gigasecond = 1e9):
    return birth_date + timedelta(seconds=_gigasecond)
