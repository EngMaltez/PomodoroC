---
title: What functions are available
author: Miguel Maltez Jose
date: 2021-04-26
---

```python
>>> dir()
[
	'node_id', 'timerSch', 'binascii', 'Btn', 'reboot', '__thonny_helper',
	'__thonny_result', 'timEx', 'BtnChild', 'axp192', 'os', 'm5base', 'axp',
	'buttonA', '__thonny_names', 'display_7seg_test', '__thonny_name', 'mode',
	'M5Led', '__VERSION__', 'sys', '__name__', 'uiflow', 'lcd', 'btnA',
	'time_ex', 'btn', 'timeSchedule', 'btnB', 'apikey', 'time', 'bm8563',
	'const', 'machine', 'display', 'rtc'
]
```

# LCD

```python
>>> dir(lcd)
[
	'__class__', 'clear', 'print', 'BLACK', 'BLUE', 'BMP', 'BOTTOM', 'CENTER',
	'COLOR_BITS16', 'COLOR_BITS24', 'CYAN', 'DARKCYAN', 'DARKGREEN','DARKGREY',
	'FONT_7seg', 'FONT_Comic', 'FONT_Default', 'FONT_DefaultSmall',
	'FONT_DejaVu18', 'FONT_DejaVu24', 'FONT_DejaVu40', 'FONT_DejaVu56',
	'FONT_DejaVu72', 'FONT_Minya', 'FONT_Small', 'FONT_Tooney', 'FONT_Ubuntu',
	'GREEN', 'GREENYELLOW', 'HSPI', 'JPG', 'LANDSCAPE', 'LANDSCAPE_FLIP',
	'LASTX', 'LASTY', 'LIGHTGREY', 'M5STACK', 'M5STICK', 'MAGENTA', 'MAROON',
	'NAVY', 'OLIVE', 'ORANGE', 'PINK', 'PORTRAIT', 'PORTRAIT_FLIP', 'PURPLE',
	'RED', 'RIGHT', 'VSPI', 'WHITE', 'YELLOW', 'arc', 'attrib7seg',
	'backlight', 'circle', 'clearwin', 'compileFont', 'deinit', 'drawCircle',
	'drawLine', 'drawPixel', 'drawRect', 'drawRoundRect', 'drawTriangle',
	'ellipse', 'fill', 'fillCircle', 'fillRect', 'fillRoundRect',
	'fillScreen', 'fillTriangle', 'font', 'fontSize', 'getCursor',
	'get_bg', 'get_fg', 'hsb2rgb', 'image', 'init', 'line', 'lineByAngle',
	'orient', 'pixel', 'polygon', 'println', 'qrcode', 'rect', 'resetwin',
	'restorewin', 'roundrect', 'savewin', 'screensize', 'setBrightness',
	'setColor', 'setCursor', 'setRotation', 'setTextColor', 'set_bg',
	'set_fg', 'setwin', 'text', 'textClear', 'textWidth', 'text_x', 'text_y',
	'tft_deselect', 'tft_readcmd', 'tft_select', 'tft_setspeed',
	'tft_writecmd', 'tft_writecmddata', 'triangle', 'winsize'
]
```

```python
>>> help(lcd)
object TFT   (160x80, Type=ST7735R, Ready: yes, Color mode: 24-bit, Clk=26666666 Hz, RdClk=8000000 Hz, Touch: no)
Pins  (miso=36, mosi=15, clk=13, cs=5, dc=23, reset=18, backlight=-1) is of type TFT
  init -- <function>
  deinit -- <function>

  pixel -- <function>
  line -- <function>
  lineByAngle -- <function>
  triangle -- <function>
  circle -- <function>
  ellipse -- <function>
  arc -- <function>
  polygon -- <function>
  rect -- <function>
  roundrect -- <function>
  clear -- <function>
  fill -- <function>
  clearwin -- <function>

  orient -- <function>
  PORTRAIT -- 0
  LANDSCAPE -- 1
  PORTRAIT_FLIP -- 2
  LANDSCAPE_FLIP -- 3


  print -- <function>
  println -- <function>
  text -- <function>
  textClear -- <function>
  setRotation -- <function>

  font -- <function>
  fontSize -- <function>
  textWidth -- <function>
  attrib7seg -- <function>
  compileFont -- <function>
  FONT_Default -- 0
  FONT_DejaVu18 -- 1
  FONT_DejaVu24 -- 2
  FONT_DejaVu40 -- 11
  FONT_DejaVu56 -- 12
  FONT_DejaVu72 -- 13
  FONT_Ubuntu -- 3
  FONT_Comic -- 4
  FONT_Minya -- 5
  FONT_Tooney -- 6
  FONT_Small -- 7
  FONT_DefaultSmall -- 8
  FONT_7seg -- 9

  image -- <function>
  hsb2rgb -- <function>

  setwin -- <function>
  resetwin -- <function>
  savewin -- <function>
  restorewin -- <function>
  screensize -- <function>
  winsize -- <function>

  get_fg -- <function>
  get_bg -- <function>
  set_fg -- <function>
  set_bg -- <function>
  setColor -- <function>
  setTextColor -- <function>

  text_x -- <function>
  text_y -- <function>


  setCursor -- <function>
  getCursor -- <function>

  fillScreen -- <function>
  drawPixel -- <function>
  drawLine -- <function>
  drawRect -- <function>
  fillRect -- <function>
  drawCircle -- <function>
  fillCircle -- <function>
  drawTriangle -- <function>
  fillTriangle -- <function>
  drawRoundRect -- <function>
  fillRoundRect -- <function>

  setBrightness -- <function>
  backlight -- <function>

  qrcode -- <function>

  tft_setspeed -- <function>
  tft_select -- <function>
  tft_deselect -- <function>
  tft_writecmd -- <function>
  tft_writecmddata -- <function>
  tft_readcmd -- <function>

  M5STACK -- 6
  M5STICK -- 4
  CENTER -- -9003
  RIGHT -- -9004
  BOTTOM -- -9004
  LASTX -- 7000
  LASTY -- 8000


  BLACK -- 0
  NAVY -- 128
  DARKGREEN -- 32768
  DARKCYAN -- 32896
  MAROON -- 8388608
  PURPLE -- 8388736
  OLIVE -- 8421376
  LIGHTGREY -- 12632256
  DARKGREY -- 8421504
  BLUE -- 255
  GREEN -- 65280
  CYAN -- 65535
  RED -- 16515072
  MAGENTA -- 16515327
  YELLOW -- 16579584
  WHITE -- 16579836
  ORANGE -- 16557056
  GREENYELLOW -- 11336748
  PINK -- 16564426

  COLOR_BITS16 -- 16
  COLOR_BITS24 -- 24
  JPG -- 1
  BMP -- 2
  HSPI -- 1
  VSPI -- 2
```

### Colors

* BLACK
* RED
* GREEN
* YELLOW
* BLUE
* MAGENTA
* CYAN
* WHITE
* DARKCYAN
* DARKGREEN
* DARKGREY
* GREENYELLOW
* LIGHTGREY
* MAROON
* NAVY
* OLIVE
* ORANGE
* PINK
* PURPLE


### Fonts

* FONT_7seg
* FONT_Comic
* FONT_Default
* FONT_DefaultSmall
* FONT_DejaVu18
* FONT_DejaVu24
* FONT_DejaVu40
* FONT_DejaVu56
* FONT_DejaVu72
* FONT_Minya
* FONT_Small
* FONT_Tooney
* FONT_Ubuntu

# Axp192

```
CURRENT_700MA -- 7
CURRENT_630MA -- 6
CURRENT_550MA -- 5
CURRENT_450MA -- 4
CURRENT_360MA -- 3
CURRENT_280MA -- 2
CURRENT_190MA -- 1
CURRENT_100MA -- 0
__module__ -- hw.axp192
__qualname__ -- Axp192
__init__ -- <function __init__ at 0x3ffe5490>
_read13Bit -- <function _read13Bit at 0x3ffe5b80>
_read12Bit -- <function _read12Bit at 0x3ffe5b70>
_regChar -- <function _regChar at 0x3ffe5b50>
_read16Bit -- <function _read16Bit at 0x3ffe5b90>
deinit -- <function deinit at 0x3ffe5ba0>
getChargeState -- <function getChargeState at 0x3ffe5970>
getTempInAXP192 -- <function getTempInAXP192 at 0x3ffe5a90>

getVBusVoltage -- <function getVBusVoltage at 0x3ffe5a70>
getVBusCurrent -- <function getVBusCurrent at 0x3ffe5a80>

getVinVoltage -- <function getVinVoltage at 0x3ffe5a50>
getVinCurrent -- <function getVinCurrent at 0x3ffe5a60>

getBatVoltage -- <function getBatVoltage at 0x3ffe5a30>
getBatCurrent -- <function getBatCurrent at 0x3ffe5a40>

btnState -- <function btnState at 0x3ffe5b10>
setLcdBrightness -- <function setLcdBrightness at 0x3ffe5af0>

setLDO2Volt -- <function setLDO2Volt at 0x3ffe5ab0>
setLDO2State -- <function setLDO2State at 0x3ffe5ad0>
setLDO3Volt -- <function setLDO3Volt at 0x3ffe5ac0>
setLDO3State -- <function setLDO3State at 0x3ffe5ae0

setChargeState -- <function setChargeState at 0x3ffe5980>
setChargeCurrent -- <function setChargeCurrent at 0x3ffe5b00>

powerAll -- <function powerAll at 0x3ffe5960>
powerOff -- <function powerOff at 0x3ffe5aa0>
```
