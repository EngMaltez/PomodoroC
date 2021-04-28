from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x111111)


title0 = M5Title(title="Watch", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0f690f)
date_text = M5TextBox(0, 20, "yyyy-mm-dd", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
time_text = M5TextBox(79, 40, "HH:MM:SS", lcd.FONT_Ubuntu,0xFFFFFF, rotate=90)
label2 = M5TextBox(0, 90, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
vbatt = M5TextBox(0, 150, "vbatt", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
ibatt = M5TextBox(40, 150, "Ibatt", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
temperature_text = M5TextBox(32, 130, "temp.", lcd.FONT_Default,0xFFFFFF, rotate=0)
battlevel = M5TextBox(0, 130, "level", lcd.FONT_Default,0xFFFFFF, rotate=0)

def displayDateTime():
  now = rtc.now()
  date_text.setText("{}-{:02d}-{:02d}".format(*now[:3]))
  time_text.setText("{:02d}:{:02d}:{:02d}".format(*now[3:]))


def displayBatteryStatus():
  vbatt.setText(str((("%.2f"%float((axp.getBatVoltage()))) + 'V')))
  ibatt.setText(str((("%.0f"%float((axp.getBatCurrent()))) + 'mA')))
  temperature_text.setText(str((("%.1f"%float((axp.getTempInAXP192()))) + 'C')))
  # battlevel.setText(str("nice"))

def buttonA_wasPressed():
  M5Led.on()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_wasReleased():
  M5Led.off()
  pass
btnA.wasReleased(buttonA_wasReleased)


setScreenColor(0x000000)
axp.setLcdBrightness(50)
while True:
  title0.setTitle('Watch')
  for i in range(1, 6):
    displayDateTime()
    displayBatteryStatus()
    wait_ms(200)
    label2.setText(str(i))
  wait_ms(2)
