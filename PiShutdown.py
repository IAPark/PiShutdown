
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)


GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.wait_for_edge(24, GPIO.RISING)
os.system("poweroff")
