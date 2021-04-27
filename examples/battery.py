"""Report battery power values.

@author Miguel Maltez Jose
@date 20210426
"""
import utime

def printCurrents():
	print(axp.getBatCurrent(), axp.getVBusCurrent(), axp.getVinCurrent())

def avgVinCurrent():
	sum = 0.0
	for i in range(10):
		utime.sleep_ms(5)
		sum += axp.getVinCurrent()
	return sum / 10

def currentVsLcd():
	for bright in range(0, 101, 2):
		axp.setLcdBrightness(bright)
		utime.sleep_ms(100)
		current = axp.getVinCurrent()
		print(bright, current, sep="\t")

def get_currents():
	i_bat = axp.getBatCurrent()
	i_vin = axp.getVinCurrent()
	i_vbus = axp.getVBusCurrent()
	return {"i_bat": i_bat, "i_vin": i_vin, "i_vbus": i_vbus}

def get_voltages():
	v_bat = axp.getBatVoltage()
	v_vin = axp.getVinVoltage()
	v_vbus = axp.getVBusVoltage()
	return {"v_bat": v_bat, "v_vin": v_vin, "v_vbus": v_vbus}

def set_lcd_brightness(bright):
	axp.setLcdBrightness(bright)


