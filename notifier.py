#!/usr/bin/env python3

import shutil
import pync

du = shutil.disk_usage("/")
rate = du.free/du.total*100

if rate <= 10:
    #pop-up comes here
    pync.notify('Take care, your disk is getting full. Your current rate is {}'.format(rate))
