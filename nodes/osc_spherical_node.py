#!/usr/bin/env python

import osc_spherical.osc

c = osc_spherical.osc.OpenSphericalCamera("192.168.50.250")



print(c.setOption("captureMode","image"))
result = c.takePicture()

print (result)
