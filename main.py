import board
import digitalio
from analogio import AnalogOut, AnalogIn
import time
import microcontroller
import math

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
#analog output pins
analog_out_1 = AnalogOut(board.A3)
analog_out_2 = AnalogOut(board.A0)
#analog input pins
temp_sensor = AnalogIn(board.A4)
PD1 = AnalogIn(board.A1)
PD2 = AnalogIn(board.A2)
# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    analog_out_1.value = 65535
    analog_out_2.value = 65535
    led.value = True
    print(getVoltage(PD1), getVoltage(PD2), getVoltage(temp_sensor))

    time.sleep(0.0004)
    led.value = False
    time.sleep(0.0004)

