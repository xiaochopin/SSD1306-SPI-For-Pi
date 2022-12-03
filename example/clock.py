# 修改自https://make.quwj.com/project/148

import adafruit_ssd1306
import board
import busio
import digitalio
import time
from PIL import Image, ImageDraw, ImageFont

BORDER = 5

# SPI初始化
# pin脚信息在board库里，是BCM模式
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D19)
dc_pin = digitalio.DigitalInOut(board.D26)
cs_pin = digitalio.DigitalInOut(board.CE0)

oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)

# 初始化 清除屏幕信息
oled.fill(0)
oled.show()

# 创建一个空白的图像
# 确保用“1”表示 1bit 的颜色
image = Image.new('1', (128,64))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,128,64), outline=0, fill=0)

font = ImageFont.truetype('lcd.ttf', 32)
font16 = ImageFont.truetype('date.ttf', 16)
try:
    while True:
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        tb=time.strftime("%H:%M:%S", time.localtime())
        ts=time.strftime("%a %b %Y", time.localtime())
        draw.text((10,14),str(tb), font=font, fill=255)
        draw.text((15,46),str(ts), font=font16, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(.1)
except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
