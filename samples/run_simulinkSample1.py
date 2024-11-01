#!/usr/bin/env python
"""
Sample script that uses the RunSimulinkPkg package created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

import RunSimulinkPkg
# Import the matlab module only after you have imported 
# MATLAB Compiler SDK generated Python modules.
import matlab

try:
    my_RunSimulinkPkg = RunSimulinkPkg.initialize()
except Exception as e:
    print('Error initializing RunSimulinkPkg package\\n:{}'.format(e))
    exit(1)

try:
    aIn = matlab.double([0.1], size=(1, 1))
    bIn = matlab.double([-130], size=(1, 1))
    cOut = my_RunSimulinkPkg.run_simulink(aIn, bIn)
    print(cOut, sep='\\n')
except Exception as e:
    print('Error occurred during program execution\\n:{}'.format(e))

my_RunSimulinkPkg.terminate()