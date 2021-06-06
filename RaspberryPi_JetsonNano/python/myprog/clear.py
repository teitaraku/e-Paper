#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from waveshare_epd import epd7in5b_V2
import sys
import os

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("init and Clear")
    epd = epd7in5b_V2.EPD()
    epd.init()
    epd.Clear()
    time.sleep(2)

    logging.info("Goto Sleep...")
    epd.sleep()

    logging.info("Finish.")

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
