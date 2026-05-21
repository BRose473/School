import datetime
import time
from CheckActive import check_active

current_time = ""

active = check_active()
while active == True:
    new_time = datetime.datetime.now().strftime("%B %d %I:%M %p")

    if current_time != new_time:
        current_time = new_time
        print(current_time)

    time.sleep(60)

    active = check_active()
    