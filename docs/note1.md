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
['BLACK', 'BLUE', 'CYAN', 'DARKCYAN', 'DARKGREEN','DARKGREY', 'GREEN', 'GREENYELLOW', 'LIGHTGREY', 'MAGENTA', 'MAROON', 'NAVY', 'OLIVE', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'WHITE', 'YELLOW']
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
