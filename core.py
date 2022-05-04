import serial
import serial.tools.list_ports
import time

class LedDriver:
    def __init__(self, port=None, baudrate=9600, timeout=0.1):

        # Find ONE serial port and assume it is the arduino

        if port is None:
            portlist = serial.tools.list_ports.comports()
            for portName in portlist:
                print(portName)
                if 'ttyACM' in str(portName):
                    port = str(portName).split('-')[0].strip()
                    print(port)
                    break

        print('I am assuming the Arduino is connected to port', port)

        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

        self.arduino = serial.Serial(port=port, baudrate=9600, timeout=0.1)

        self.states = [0,0,0,0,0,0]
        self.start_code = 7
        self.end_code = 9

    def set_relays(self, states):
        assert len(states) == 6

        # The logic of the driver is flipped
        states = list([1 if x==0 else 0 for x in states])

        new_states = [self.start_code,] + states + [1, 1, self.end_code]
        self.arduino.write(bytearray(new_states))


if __name__ == "__main__":

    ld = LedDriver()

    time.sleep(3)
    relay_states = [1,0,0,0,0,0]
    ld.set_relays(relay_states)

    time.sleep(3)
    relay_states = [1,1,0,0,0,0]
    ld.set_relays(relay_states)

    time.sleep(3)
    relay_states = [0,0,0,0,0,1]
    ld.set_relays(relay_states)

    time.sleep(3)
    relay_states = [0,0,0,0,1,1]
    ld.set_relays(relay_states)

    time.sleep(3)
    relay_states = [0,0,1,0,0,0]
    ld.set_relays(relay_states)

    time.sleep(3)
    relay_states = [0,0,1,1,0,0]
    ld.set_relays(relay_states)




    # data = arduino.readline()
    # print(data)
