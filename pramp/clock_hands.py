""" find the smallest angle between 2 hands of a clock

    >>> clock_hands(12, 30)
    165.0

    >> clock_hands(3,30)
    75.0

    >> clock_hands(9,60)
    90.0

"""

def clock_hands(hour, minute):
    """ calculate the smallest angle between 2 hands of a clock """

    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 0

    hour_angle = (hour * 60 + minute) * 0.5  # convert hour to minutes to account for how late in the hour
    minute_angle = minute * 6  # each minute equates to 6 degrees (from 12)

    angle = abs(hour_angle - minute_angle)
    angle = min(360-angle, angle)

    return angle


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"