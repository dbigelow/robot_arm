#!/usr/bin/env python

import SeqEditor


tmp = SeqEditor.SeqEditor()



tmp.runPose()

  
tmp.setPose([512, 512, 800, 724, 512], 1000)
tmp.runPose()
 
 
tmp.setPose([900, 512, 512, 512, 90], 1500)
tmp.runPose()
 
tmp.setPose([500, 512, 112, 512, 90], 1500)
tmp.runPose()