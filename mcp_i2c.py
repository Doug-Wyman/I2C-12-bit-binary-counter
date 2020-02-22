"""THIS CODE IS OBSOLETE! Changes promised!!.
I am attempting to not just rewrite but make it
as close to PEP-8 as possible."""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mcpcounter.py
#  
#  Copyright 2018 Doug Wyman <doug@stretchmain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import smbus

class counter():
    def __init__(self,busnum, deviceaddr, **kwargs):
        if busnum is None:
            self.busnum = int(1)
        else:
            self.busnum = busnum
        if deviceaddr is None:
            self.deviceaddr = int(0x20)
        else:
            self.deviceaddr = deviceaddr
        chip = smbus.SMBus(int(self.busnum))
        chip.write_word_data(int(self.deviceaddr), 0x00, 4095) #set the first 12 bits to inputs 
        self.i2c = chip
        self.i2c.write_byte_data(int(self.deviceaddr), 19, 208) # Set the LED on, NOT reset, and enable count 
        self.isready = 'I am ready'
    def getcount(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp & 176
        mask2 = tmp & 240
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask2))
        return self.i2c.read_word_data(int(self.deviceaddr), 18) & 4095
        
    def resetcount(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp & 112
        mask2 = tmp & 240
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask2))
        return self.i2c.read_word_data(int(self.deviceaddr), 18) & 4095
        
    def LEDon(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp | 16
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        return "Set Pin High"

    def LEDoff(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp & 224
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        return "Set Pin Low"
        
    def AUXon(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp | 32
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        return "Set Pin High"

    def AUXoff(self):
        tmp = self.i2c.read_byte_data(self.deviceaddr,19) # get the current LED and aux setting
        mask1 = tmp & 208
        self.i2c.write_byte_data(int(self.deviceaddr), 19, int(mask1))
        return "Set Pin Low"

print("loaded device")

