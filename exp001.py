"""Experiment 1, detecting a button press and time between two presses.

@author Miguel Maltez Jose
@date 20210419
"""
import time
from machine import Pin
from m5stack import btnA

redled = Pin(10, Pin.OUT)

tmr_running = False


def button_was_pressed():
	global redled
	global tmr_running, tmr_start
	if tmr_running:
		delta = time.ticks_diff(time.ticks_us(), tmr_start)
		tmr_running = False
		print(delta)
	else:
		tmr_start = time.ticks_us()
		tmr_running = True
	redled.value(0)

def button_was_released():
	global redled
	redled.value(1)

btnA.wasPressed(button_was_pressed)
btnA.wasReleased(button_was_released)

lcd.setRotation(1)
lcd.print("Experiment 1", 0,0)
