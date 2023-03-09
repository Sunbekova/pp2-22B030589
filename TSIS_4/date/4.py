#Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

today = datetime.now()
tmrw = today + timedelta(days=1)

diff = (today - tmrw).total_seconds()
print(diff)