import asyncio
import time

def alarm():
    print("Alarm! Time to wake up!")
    print("Playing alarm sound...")
    loop.call_later(1, alarm)  # Schedule the alarm to repeat every second

def door_bell():
    print("Ding Dong! Someone is at the door!")
    print("Playing doorbell sound...")
    

def phonecall():
    print("Ringing! You have an incoming call!")
    print("Playing ringtone sound...")
    loop.stop()
loop = asyncio.get_event_loop()

loop.call_later(1, alarm)
loop.call_later(2, door_bell)
loop.call_later(6, phonecall)

print("Starting the event loop...")
loop.run_forever()

print("Event loop has stopped. Exiting the program.")
