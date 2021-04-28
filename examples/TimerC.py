from m5stack import *
from m5ui import *
from uiflow import *
import hat
import time
import hat

setScreenColor(0x111111)

hat_spk0 = hat.get(hat.SPEAKER)



title0 = M5Title(title="Timer", x=1 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
button_time_label = M5TextBox(4, 72, "Text", lcd.FONT_Ubuntu,0xFFFFFF, rotate=0)
rectangle0 = M5Rect(10, 140, 60, 10, 0xFFFFFF, 0xFFFFFF)
rectangle1 = M5Rect(10, 120, 60, 10, 0xFFFFFF, 0xFFFFFF)
rectangle2 = M5Rect(10, 100, 60, 10, 0xFFFFFF, 0xFFFFFF)
timer_m = M5TextBox(2, 25, "22", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
timer_s = M5TextBox(41, 25, "00", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
colon = M5TextBox(33, 22, ":", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
timer_label = M5TextBox(41, 72, "2500", lcd.FONT_Ubuntu,0xFFFFFF, rotate=0)
batt_label = M5TextBox(48, 4, "100%", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
msg_label = M5TextBox(9, 55, "message", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)

from numbers import Number

button_time = None
timer_count = None
button_press_count = None
timer_running = None

def alarm1():
  global button_time, timer_count, button_press_count, timer_running
  M5Led.on()
  hat_spk0.setVolume(3)
  hat_spk0.tone(4000, 200)
  wait_ms(100)
  hat_spk0.tone(6000, 200)
  wait_ms(100)
  hat_spk0.tone(8000, 200)
  M5Led.off()

def render_timer():
  global button_time, timer_count, button_press_count, timer_running
  timer_m.setText(str(int((timer_count / 60))))
  timer_s.setText(str(timer_count % 60))


def buttonA_wasPressed():
  global button_time, timer_count, button_press_count, timer_running
  rectangle0.setBgColor(0xff0000)
  timerSch.run('button_timer', 400, 0x00)
  button_press_count = (button_press_count if isinstance(button_press_count, Number) else 0) + 1
  if button_press_count==2:
    button_time_label.setColor(0x3366ff)
  elif button_press_count==3:
    button_time_label.setColor(0xffffff)
  else:
    pass
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_wasReleased():
  global button_time, timer_count, button_press_count, timer_running
  timerSch.stop('button_timer')
  if button_time < 2:
    if timer_running:
      timerSch.stop('timer1')
      timer_label.setColor(0x999900)
      timer_running = False
    else:
      timerSch.run('timer1', 1000, 0x00)
      timer_label.setColor(0x33ff33)
      timer_running = True
  button_time = 0
  rectangle0.setBgColor(0x000000)
  rectangle1.setBgColor(0x000000)
  rectangle2.setBgColor(0x000000)
  pass
btnA.wasReleased(buttonA_wasReleased)

@timerSch.event('button_timer')
def tbutton_timer():
  global button_time, timer_count, button_press_count, timer_running
  button_time = (button_time if isinstance(button_time, Number) else 0) + 1
  button_press_count = 0
  if not timer_running:
    if button_time==4:
      rectangle2.setBgColor(0xff0000)
      timer_count = 1500
      timer_label.setColor(0xff9900)
    elif button_time==2:
      rectangle1.setBgColor(0xff0000)
      timer_count = 300
      timer_label.setColor(0xff9900)
    elif button_time==6:
      timer_count = 5
      timer_label.setColor(0xff6600)
    else:
      pass
  pass

@timerSch.event('timer1')
def ttimer1():
  global button_time, timer_count, button_press_count, timer_running
  timer_count = (timer_count if isinstance(timer_count, Number) else 0) + -1
  pass


axp.setLcdBrightness(50)
button_time = 0
timer_count = 3
batt_label.setFont(lcd.FONT_Default)
while True:
  render_timer()
  timer_label.setText(str(timer_count))
  button_time_label.setText(str(button_time))
  batt_label.setText(str("%.2f"%((axp.getBatVoltage()))))
  if axp.getChargeState():
    batt_label.setColor(0x33ff33)
    msg_label.setText('charging')
  else:
    batt_label.setColor(0xffffff)
  if timer_running and timer_count <= 0:
    timer_running = False
    timerSch.stop('timer1')
    timer_label.setColor(0x999900)
    alarm1()
  wait_ms(40)
  wait_ms(2)
