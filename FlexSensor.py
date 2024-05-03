class FlexSensors :
    def __init__(self, finger, pinA, pinB) :
        self.finger = finger
        self.pinA = pinA
        self.pinB = pinB
        self.value = None

    def analogread(self):
        print(f"")
        