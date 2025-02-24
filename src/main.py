# Test script for model rail board
from signal import *

# Track diagram
#
#            o>
#        CH5 | 
# |=====B6===== =.
#                 |          o>
#                 |          | CH2
#                 x=B4= ===B3== ===B1==|
#            o>   |      | CH3   | CH1
#        CH4 |    |     <o      <o
# |=====B5===== =`
#
# CH# are the signals
# B# are the block (B1 was a miscount...)
#
# Need a declarative language, something like
# CH5 is in B6 and it protects B4 and B3
# CH3 is in B3 and it protects B6 or B5
# However, if we route from signal to signal, and include the terminating blocks
# I think we can reserve paths? Believe this is how it works IRL
# So something like a path from CH5 to end block (beyond CH1)
# Needs to set CH5, CH2
# Needs to check B4 B3 B1 are clear
# Needs to ensure CH3 CH1 are already at danger

# Setup:

ch1 = RedGreenSignal('CH1', 16, 17)
ch2 = RedGreenSignal('CH2', 18, 19)
ch3 = RedGreenSignal('CH3', 20, 21)
ch4 = RedGreenSignal('CH4', 15, 14)
ch5 = RedGreenSignal('CH5', 13, 12)

RedGreenSignal.setAllRed([ch1, ch2, ch3, ch4, ch5])
# Set a path from CH5 to CH1
ch5.setGreen()
ch2.setGreen()

