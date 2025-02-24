import machine

class BaseSignal:

    BLANK = 0

    state = None
    id = None

    def __init__(self, id):
        self.id = id

    def logInfo(self, text):
        print("INFO %s %s" % (self.id, text))

    def logWarning(self, text):
        print("WARNING %s %s" % (self.id, text))

    def getId(self):
        return self.id

    def getState(self):
        return self.state
    
    def getStateLabel(self):
        return 'BLANK'
    
    def setBlank(self):
        # No lights are illuminated
        self.state = self.BLANK
    
    def test(self):
        # Nothing to test since we aren't real
        self.logInfo("We exist but have no state")
    
    def testAll(signals):
        # Static testing script
        for signal in signals:
            signal.test()

    




class RedGreenSignal(BaseSignal):
    RED = 1
    GREEN = 2

    gpio_red = None
    gpio_green = None

    def __init__(self, id, red_pin, green_pin):
        super().__init__(id)
        # We need to assign the red and green GPIOs accordingly:
        # Leave all lights off by default (initial state will set one)
        self.gpio_red = machine.Pin(red_pin, machine.Pin.OUT)
        self.gpio_green = machine.Pin(green_pin, machine.Pin.OUT)
        self.gpio_red.off()
        self.gpio_green.off()
        self.setBlank()



    def getStateLabel(self):
        state = self.getState()
        if state == self.RED:
            return 'RED'
        if state == self.GREEN:
            return 'GREEN'
        super().getStateLabel()

    def setRed(self):
        if self.state != self.RED:
            print("WARNING Setting to RED when light was %s" % (self.getStateLabel()))
        self.state = self.RED
        self.setLeds()

    def setGreen(self):
        self.state = self.GREEN
        self.setLeds()

    def setLeds(self):
        # Update the lights to reflect the current state
        # Verbose for legibility right now
        if self.state == self.RED:
            self.gpio_red.on()
        else:
            self.gpio_red.off()

        if self.state == self.GREEN:
            self.gpio_green.on()
        else:
            self.gpio_green.off()


    def test(self):
        self.gpio_green.on()
        self.gpio_red.on()

    # Static functiony goodness:

    def setAllRed(signals):
        # Set all signals in this list to red
        for signal in signals:
            signal.setRed()

