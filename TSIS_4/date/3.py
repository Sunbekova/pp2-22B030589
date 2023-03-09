#Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta

today = datetime.now()
today = today.replace(microsecond=0)

print(today)