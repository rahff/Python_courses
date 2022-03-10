from datetime import datetime

une_date = datetime(2022, 5, 21, 15, 36, 15)

print(une_date.strftime("%A, %d. %B %Y %I:%M%p"))
# Saturday, 21. May 2022 03:36PM

print(une_date.strftime("%A, %d. %B %Y %H:%M:%S"))
# Saturday, 21. May 2022 15:36:15