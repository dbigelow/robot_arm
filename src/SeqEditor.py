#!/usr/bin/env python

""" 
  PyPose: Bioloid pose system for arbotiX robocontroller
  Copyright (c) 2008-2010 Michael E. Ferguson.  All right reserved.

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software Foundation,
  Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from driver import *
from time import sleep
###############################################################################
# Sequence editor window
class SeqEditor():
    
    def __init__(self):
        self.port = Driver("/dev/ttyUSB0", 38400, True) # w/ interpolation
        self.pose = [512, 512, 512, 512, 512]
        self.dt = 1000
        print("initializing.....")
        sleep(7)
        print("ready")
        
    def setPose(self, pose, dt):
        self.pose = pose
        self.dt = dt
    
    def runPose(self, e=None):
        sendPose = []#[[i%256, i>>8] for i in self.pose]
        for i in self.pose:
            sendPose += [i%256, i>>8]
        
        """ download poses, seqeunce, and send. """
        if self.port != None: 
            tranDL = []
            tranDL.append(0)
            tranDL.append(self.dt%256)
            tranDL.append(self.dt>>8)
            tranDL.append(255)      # notice to stop
            tranDL.append(0)        # time is irrelevant on stop    
            tranDL.append(0)
            # set pose size -- IMPORTANT!
            print "Setting pose size at " + str(5)
            self.port.execute(253, 7, [5])
#             sleep(.5)
            # send poses            
            print "Sending pose to position " + str(0)
            tst = [0] + sendPose
            self.port.execute(253, 8, [0] + sendPose)
#             sleep(.5) 
            print "Sending sequence: " + str(tranDL)
            # send sequence and play            
            self.port.execute(253, 9, tranDL)
#             sleep(.5) 
            self.port.execute(253, 10, list())
            sleep(.001*self.dt)
            print "playing sequence"
#             else:
#                 self.parent.sb.SetBackgroundColour('RED')
#                 self.parent.sb.SetStatusText("Select a Sequence",0) 
#                 self.parent.timer.Start(20)                
        else:
            print("No port open")
