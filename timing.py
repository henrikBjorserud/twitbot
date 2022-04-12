from datetime import datetime
from suntime import Sun, SunTimeException

latitude = 57.79
longitude = 11.96


def wait_randomly_or_wait_for_sunrise():
    sun = Sun(latitude, longitude)
    time_right_now = datetime.now()
    # Get today's sunrise and sunset in UTC
    sr = sun.get_sunrise_time()
    ss = sun.get_sunset_time()
    
    now_hour = int(time_right_now.strftime('%H'))
    sunrise_hour = int(sr.strftime('%H')) + 2
    sunset_hour = int(ss.strftime('%H')) + 2

    if sunrise_hour < now_hour and now_hour < sunset_hour:
        print('daytime')
    else:
        print('nighttime')

wait_randomly_or_wait_for_sunrise()
