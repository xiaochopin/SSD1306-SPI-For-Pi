# SSD1306-SPI-For-Pi

## 硬件

1.买一个SSD1306(7针SPI)(废话)

2.连接到树莓派上

| SSD1306 | Pi |
|---|---|
| GND | GND |
| VCC | 3.3V |
| CS | CE0 |
| RST | GPIO24 |
| DC | GPIO25 |
| D0 | SCLK |
| D1 | MOSI |

## 软件

1.在树莓派上安装基于`Debian`的`Raspbian`（其它系统有玄学问题）.

2.更新软件包.

```
apt-get update
apt-get upgrade
```

3.安装依赖和库.

```
//我也不知道哪些是有效操作,反正都做了.

git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git

cd Adafruit_Python_SSD1306

python3 setup.py install

apt install python3-pil

apt-get install build-essential python-dev python-pip

pip install RPi.GPIO    //树莓派Python的GPIO库

pip install adafruit-circuitpython-ssd1306    //SSD1306 Library库安装

apt-get install python3-pi

```

4.设置

运行`sudo raspi-config`.

选择`Interfacing Options`.

选择`SPI`.

选择`Yes`.

5.修改

根据注释修改`ssd1306.py`第19,20行.

## 引用

+ [树莓派 SPI/IIC 点亮OLED—SSD1306模块](https://blog.csdn.net/weixin_43123169/article/details/119645175)
