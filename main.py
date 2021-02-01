# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()

while True:
    percent = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(percent)+"% Battery remaining",
        timeout=100,
    )

    time.sleep(60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
