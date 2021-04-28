"""A digital clock

@author Miguel Maltez Jose
@date 20210428
"""
import json
import time
import network
import socket
import struct
import machine
from m5stack import lcd, axp
from flowlib.hw.bm8563 import Bm8563

lcd_brightness = 40
ALARM_VOLUME_RESET_VALUE = 2
alarm_volume = ALARM_VOLUME_RESET_VALUE

def connectToWifi(configfn="config.json"):
	"""Setup WiFi."""
	with open(configfn) as configfile:
		config = json.load(configfile)
	sta_if = network.WLAN(network.STA_IF)
	sta_if.active(True)
	lcd.font(lcd.FONT_Default)
	lcd.print("WiFi " + "active" if sta_if.active() else "inactive", 0,0, lcd.YELLOW)
	trycount = 0
	while not sta_if.isconnected():
		sta_if.connect(config['wifi']['ssid'], config['wifi']['password'])
		lcd.print(".")
		time.sleep(1)
		trycount += 1
		if trycount > 10:
			break
	return sta_if

def getNTPTime(host = "pool.ntp.org", toffset=0):
	"""Get time from Network Time Protocol. toffset is time offset in seconds, e.g. +05:30 = 5.5*3600"""
	# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
	NTP_DELTA = 3155673600
	NTP_QUERY = bytearray(48)
	NTP_QUERY[0] = 0x1B
	addr = socket.getaddrinfo(host, 123)[0][-1]
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.settimeout(1)
		res = s.sendto(NTP_QUERY, addr)
		msg = s.recv(48)
	finally:
		s.close()
	val = struct.unpack("!I", msg[40:44])[0]
	return val - NTP_DELTA + toffset

def updateRTC(toffset=0):
	"""Get NTP and set the RTC. toffset is time offset in seconds."""
	rtcchip = Bm8563()
	lt = getNTPTime(toffset=toffset)
	tm = time.localtime(lt)
	rtcchip.setTime(*tm[0:6])
	machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

class Clock():
	def __init__(self):
		self.hour, self.minute, self.second = 0, 0, 0
		self.dirty = True
		self.color = lcd.RED
	def update(self):
		lt = time.localtime()
		if (self.second != lt[5] or self.minute != lt[4] or self.hour != lt[3]):
			self.hour, self.minute, self.second = lt[3:6]
			self.setDirty()
	def render(self):
		lcd.font(lcd.FONT_7seg, dist=8, width=2)
		_, fh = lcd.fontSize()
		lcd.print("%02d:%02d:%02d" % (self.hour, self.minute, self.second), lcd.CENTER, 80 - fh, self.color)
		self.dirty = False
	def setDirty(self):
		self.dirty = True
	def isDirty(self):
		return self.dirty

class Calendar():
	def __init__(self):
		self.year, self.month, self.mday = 0,0,0
		self.dirty = True
		self.color = lcd.RED
	def update(self):
		lt = time.localtime()
		self.year, self.month, self.mday = lt[:3]
	def render(self):
		lcd.font(lcd.FONT_Ubuntu, dist=8, width=1)
		lcd.print("%04d-%02d-%02d" % (self.year, self.month, self.mday), lcd.CENTER, 0, self.color)
	def setDirty(self):
		self.dirty = True
	def isDirty(self):
		return self.dirty

# Buttons

def buttonB_wasPressed():
	global lcd_brightness
	lcd_brightness += 10
	if lcd_brightness > 100:
		lcd_brightness = 0
	axp.setLcdBrightness(lcd_brightness)
btnB.wasPressed(buttonB_wasPressed)

# MAIN

clock = Clock()
calendar = Calendar()
# label_bright = M5TextBox(0, 0, "%3d" % lcd_brightness, lcd.FONT_Default, lcd.GREENYELLOW, rotate=0)
# batt_label = M5TextBox(120, 30, "%.2fV" % 0.0, lcd.FONT_DefaultSmall, lcd.DARKCYAN, rotate=0)

def setup():
	global lcd_brightness
	lcd.setRotation(1)
	axp.setLcdBrightness(lcd_brightness)
	lcd.clear(0x000000)
	lcd.set_bg(0x070707)

	year = time.localtime()[0]
	if year < 2001:
		wifi = connectToWifi()
		if wifi.active():
			updateRTC(toffset=3600)
			wifi.active(False)
		time.sleep(3)

	lcd.clear(0x000000)

def loop():
	global calendar
	global clock
	while True:
		clock.update()
		calendar.update()
		if clock.isDirty():
			clock.render()
		if calendar.isDirty():
			calendar.render()
		# batt_label.setText("%.2fV"%((axp.getBatVoltage())))
		# if axp.getChargeState():
			# batt_label.setColor(0x33ff33)
		# else:
			# batt_label.setColor(0xaaaaaa)
		time.sleep_ms(200)

setup()
loop()
