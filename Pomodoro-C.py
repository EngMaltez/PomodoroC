"""Pomodoro timer.

* Press once to start
* Press again to stop
* When stopped hold to reset time until it reaches desired value.
* Red LED lights up when 0 is reached.

@author Miguel Maltez Jose
@date 20210324
"""

from m5stack import *
from m5ui import *
from uiflow import *
lcd.setRotation(0)
import time

setScreenColor(0x000000)


val = None
button_counter = None
countdown_time = None
soundalarm_flag = None
countdown_running = None
last_value = None
LONGPRESS_THRESHOLD = 4
countdown_textcolor = 0xFFFFFF


circle0 = M5Circle(40, 80, 16, 0x000000, 0xFFFFFF)
bar1 = M5Rect(2, 151, 76, 8, 0x000000, 0xFFFFFF)
bar2 = M5Rect(2, 140, 76, 8, 0x000000, 0xFFFFFF)
bar3 = M5Rect(2, 129, 76, 8, 0x000000, 0xFFFFFF)
# label_countdown = M5TextBox(6, 25, "0000", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Pomodoro", x=3, fgcolor=0xFFFFFF, bgcolor=0xFF4500)
label0 = M5TextBox(72, 70, "counter", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=90)

vbatt = M5TextBox(0, 112, "vbatt", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
ibatt = M5TextBox(40, 112, "Ibatt", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
temperature_text = M5TextBox(12, 64, "temp.", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=90)

from numbers import Number

def setCountdownColor(color):
  global countdown_textcolor
  countdown_textcolor = color

def startCountdown():
  global val, button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD
  timerSch.run('countdownTimer', 100, 0x00)
  countdown_running = True
  circle0.setBgColor(lcd.BLACK)
  title0.setBgColor(lcd.NAVY)
  if countdown_time > 0:
    setCountdownColor(lcd.GREEN)
  else:
    setCountdownColor(lcd.RED)

def stopCountdown():
  global val, button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD
  timerSch.stop('countdownTimer')
  countdown_running = False
  circle0.setBgColor(0x7f7f7f)
  title0.setBgColor(0x2F4F4F)
  if countdown_time > 0:
    setCountdownColor(lcd.OLIVE)
  else:
    setCountdownColor(lcd.MAROON)

def resetCountDown(val):
  global button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD
  countdown_time = 10 * val
  setCountdownColor(0xffcc00)

def displayCountdown():
  global val, button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD
  global countdown_textcolor
  if last_value != int((countdown_time / 10)) or last_value == 0:
    last_value = int((countdown_time / 10))
    if countdown_time < 0:
      if countdown_running:
        setCountdownColor(lcd.RED)
      else:
        setCountdownColor(lcd.MAROON)
      last_value *= -1
    lcd.font(lcd.FONT_7seg)
    lcd.attrib7seg(6, 1, False, lcd.CYAN)
    fs = lcd.fontSize()
    lcd.text(lcd.CENTER, 50-fs[1], "%02d:%02d" % (last_value / 60, last_value % 60), countdown_textcolor)


def buttonA_wasPressed():
  global button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD, val
  timerSch.run('buttonTimerA', 100, 0x00)
  soundalarm_flag = False
  M5Led.off()
  circle0.setBgColor(0x000000)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_wasReleased():
  global button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD, val
  timerSch.stop('buttonTimerA')
  bar1.setBgColor(0x000000)
  bar2.setBgColor(0x000000)
  bar3.setBgColor(0x000000)
  if button_counter < LONGPRESS_THRESHOLD:
    if countdown_running:
      stopCountdown()
    else:
      startCountdown()
  button_counter = 0
  pass
btnA.wasReleased(buttonA_wasReleased)

@timerSch.event('buttonTimerA')
def tbuttonTimerA():
  global button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD, val
  button_counter = (button_counter if isinstance(button_counter, Number) else 0) + 1
  if button_counter==2:
    bar1.setBgColor(0xff0000)
  elif button_counter==4:
    bar2.setBgColor(0xff0000)
  elif button_counter==6:
    bar3.setBgColor(0xff0000)
  else:
    pass
  if not countdown_running:
    if button_counter==LONGPRESS_THRESHOLD:
      resetCountDown(300)
    elif button_counter==(LONGPRESS_THRESHOLD * 3):
      resetCountDown(1500)
    elif button_counter==(LONGPRESS_THRESHOLD * 5):
      resetCountDown(1200)
    elif button_counter==(LONGPRESS_THRESHOLD * 7):
      resetCountDown(900)
    elif button_counter==(LONGPRESS_THRESHOLD * 9):
      resetCountDown(600)
    elif button_counter==(LONGPRESS_THRESHOLD * 12):
      resetCountDown(5)
    else:
      pass
  pass

@timerSch.event('countdownTimer')
def tcountdownTimer():
  global button_counter, countdown_time, soundalarm_flag, countdown_running, last_value, LONGPRESS_THRESHOLD, val
  countdown_time = (countdown_time if isinstance(countdown_time, Number) else 0) + -1
  if countdown_time == 0:
    soundalarm_flag = True
  pass

def displayBatteryStatus():
  vbatt.setText(str((("%.2f"%float((axp.getBatVoltage()))) + 'V')))
  ibatt.setText(str((("%.0f"%float((axp.getBatCurrent()))) + 'mA')))
  temperature_text.setText(str((("%.1f"%float((axp.getTempInAXP192()))) + 'C')))

# Main

axp.setLcdBrightness(50)
LONGPRESS_THRESHOLD = 4
countdown_running = False
soundalarm_flag = False
resetCountDown(300)
timerSch.setTimer('buttonTimerA', 100, 0x00)
timerSch.setTimer('countdownTimer', 100, 0x00)
while True:
  displayCountdown()
  label0.setText(str(countdown_time))
  displayBatteryStatus()
  if soundalarm_flag:
    M5Led.on()
    circle0.setBgColor(0xff0000)
  wait_ms(200)
  wait_ms(2)

