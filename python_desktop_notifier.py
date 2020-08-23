#  youtube.com/atozknowledgevideos

from pynotifier import Notification
#win10toast

Notification(
     title="atozknowledge.com",
     description="Welcome to atozknowledge.com , you have 3 unread messages",
     duration=25,
     urgency=Notification.URGENCY_CRITICAL
).send()
