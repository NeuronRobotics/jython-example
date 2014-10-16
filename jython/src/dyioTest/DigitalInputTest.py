#!/usr/bin/env jython
"""
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */ 
 """
#@author: eastein http://cons.truct.org/archives/jython-and-dyio.html

import sys, time

sys.path.append('../lib/nrdk-3.7.2-jar-with-dependencies.jar')

from com.neuronrobotics.sdk.dyio import DyIO
from com.neuronrobotics.sdk.dyio.peripherals import DigitalInputChannel
from com.neuronrobotics.sdk.serial import SerialConnection
from com.neuronrobotics.sdk.ui import ConnectionDialog
if __name__ == '__main__' :
        #dyio = DyIO(SerialConnection("/dev/ttyACM0"))
        #dyio.connect()
        dyio=DyIO();
        if (not ConnectionDialog.getBowlerDevice(dyio)):
            sys.exit(1)
        
        dig = DigitalInputChannel(dyio.getChannel(0))

        while True :
                print dig.isHigh()
                time.sleep(.25)