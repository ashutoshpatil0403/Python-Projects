import time
from plyer import notification

while(True):

    notification.notify(
        title="Drink Water Reminder",
        message="Himan Body Daily Requirement 3-4 Litres",
        #icon="",
        timeout=5
    )
    time.sleep(60*60)