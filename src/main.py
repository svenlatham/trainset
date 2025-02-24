# Test script for model rail board
from signal import *

# Setup:

ch1 = RedGreenSignal('CH1', 16, 17)
ch2 = RedGreenSignal('CH2', 18, 19)
ch3 = RedGreenSignal('CH3', 20, 21)
ch4 = RedGreenSignal('CH4', 15, 14)
ch5 = RedGreenSignal('CH5', 13, 12)

BaseSignal.testAll([ch1, ch2, ch3, ch4, ch5])

