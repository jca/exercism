from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):
    try:
        weekday_meetup = list(calendar.day_name).index(day_of_the_week)
    except:
        raise ValueError('Invalid day name!')

    if which[0].isdigit():
        maxday = int(which[0]) * 7
    elif which == 'last':
        maxday = calendar.monthrange(year, month)[1]
    elif which == 'teenth':
        maxday = 19
    else:
        raise ValueError('Invalid which!')

    weekday_first = date(year, month, 1).weekday()
    meetup_day = xrange(weekday_meetup - weekday_first + 1, maxday+1, 7)[-1]

    return date(year, month, meetup_day)
