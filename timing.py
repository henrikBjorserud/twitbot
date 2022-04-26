from datetime import datetime
from suntime import Sun
import quantumrandom

latitude = 57.79
longitude = 11.96


def wait_randomly_or_wait_for_sunrise():

    sun = Sun(latitude, longitude)
    time_right_now = datetime.now()
    # Get today's sunrise and sunset in UTC
    sr = sun.get_sunrise_time()
    ss = sun.get_sunset_time()

    now_hour = int(time_right_now.strftime("%H"))
    sunrise_hour = int(sr.strftime("%H")) + 2
    sunset_hour = int(ss.strftime("%H")) + 2
    random_numbers = int(quantumrandom.randint(120, 240))
    seconds_to_wait = random_numbers * 60
    night_time_hours = 24 - sunset_hour + sunrise_hour
    night_time_minutes = night_time_hours * 60
    night_time_seconds = night_time_minutes * 60

    if sunrise_hour < now_hour and now_hour < sunset_hour:
        return seconds_to_wait

    else:
        return seconds_to_wait + night_time_seconds
