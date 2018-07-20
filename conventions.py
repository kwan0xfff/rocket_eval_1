#!/usr/bin/env python
#-*- coding: utf-8 -*-

# some constants
kg2lb = 2.2046226218488 # kilograms to pounds mass
lb2kg = 1.0/kg2lb
gEarth = 9.80665        # gravity at Earth surface

# force
N2lb = 0.224808943      # Newtons to pounds

# volumes
l2gal = 0.264172        # liters to US gallons
l2ft3 = 0.0353147       # liters to cubic feet
l2m3 = 0.001            # liters to cubic meters

# power
W2BTUph = 3.41214163    # watts to BTU/hr
kW2hp = 1.34102209      # kilowatts to horsepower

# some helpful constant dictionary element names.
# put '_' at end to avoid clash with variables of same name.
name_ = 'name'          # some arbitrary text descriptor:
m_ = 'm'                # mass (e.g., payload), kg
m0_ = 'm0'              # initial mass of stage, kg
m1_ = 'm1'              # final mass of stage, kg
isp_ = 'isp'            # specific impulse, sec
dVdsrd_ = 'dVdsrd'      # delta V desired, m/s
dV_ = 'dV'              # delta V, m/s
MR_ = 'MR'              # mass ratio
Tpeak_ = 'Tpeak'        # peak thrust
Tavg_ = 'Tavg'          # average thrust

# vim: set sw=4 tw=80 :
