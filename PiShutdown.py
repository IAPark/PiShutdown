import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)


GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.5)

GPIO.wait_for_edge(13, GPIO.RISING)
print("Shutting down, NOW!")
os.system("shutdown -h now")
GPIO.cleanup()
