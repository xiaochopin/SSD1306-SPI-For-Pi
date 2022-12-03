# 修改自https://blog.csdn.net/weixin_43123169/article/details/119645175

import adafruit_ssd1306
import board
import busio
import digitalio
import time
from PIL import Image, ImageDraw, ImageFont

#屏幕长宽
WIDTH = 128 
HEIGHT = 64

BORDER = 5

# SPI初始化
# pin脚信息在board库里，是BCM模式
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D19) # 将19改为树莓派上GPIO.24对应的BCM编码
dc_pin = digitalio.DigitalInOut(board.D26) # 将26改为树莓派上GPIO.25对应的BCM编码
cs_pin = digitalio.DigitalInOut(board.CE0)

oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc_pin, reset_pin, cs_pin)

# 初始化 清除屏幕信息
oled.fill(0)
oled.show()

# 创建一个空白的图像
# 确保用“1”表示 1bit 的颜色
image = Image.new("1", (oled.width, oled.height))

# 获取绘制对象来绘制图像
draw = ImageDraw.Draw(image)

# 绘制一个白色的背景
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# 绘制一个小的内边框
draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), fill=0, outline=0)

# 加载默认样式
font = ImageFont.load_default()

# 绘制文字
text = "Hello World!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

try:
    while True:
        oled.image(image)
        oled.show()
#退出时关闭屏幕显示
except KeyboardInterrupt:
    oled.fill(0)
    oled.show()