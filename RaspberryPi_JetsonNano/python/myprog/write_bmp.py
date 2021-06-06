#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5b_V2
import time
from PIL import Image, ImageDraw, ImageFont


logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("write bmp image to epd7in5b")

    bmp_black: str = ""
    bmp_red: str = ""
    if len(sys.argv) < 2:
        logging.info("please input file name")
        exit()

    bmp_black: str = sys.argv[1]
    if 3 <= len(sys.argv):
        bmp_red: str = sys.argv[2]

    if not os.path.isfile(os.path.join(picdir, bmp_black)):
        logging.info("file not found: " + bmp_black)
        exit()
    if bmp_red and not os.path.isfile(os.path.join(picdir, bmp_red)):
        logging.info("file not found: " + bmp_red)
        exit()

    epd = epd7in5b_V2.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("write bmp file")
    image_black = Image.open(os.path.join(picdir, bmp_black))
    if bmp_red:
        image_red = Image.open(os.path.join(picdir, bmp_red))
        epd.display(epd.getbuffer(image_black), epd.getbuffer(image_red))
    else:
        epd.display(epd.getbuffer(image_black), None)

    time.sleep(2)

    logging.info("goto sleep...")
    epd.sleep()

    logging.info("finish")

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
