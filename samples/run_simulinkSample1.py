#!/usr/bin/env python
"""
Sample script that uses the RunSimulinkPkg package created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

from __future__ import print_function
import RunSimulinkPkg
import matlab

my_RunSimulinkPkg = RunSimulinkPkg.initialize()

aIn = matlab.double([0.1], size=(1, 1))
bIn = matlab.double([-10], size=(1, 1))
cOut = my_RunSimulinkPkg.run_simulink(aIn, bIn)
print(cOut, sep='\\n')

my_RunSimulinkPkg.terminate()
