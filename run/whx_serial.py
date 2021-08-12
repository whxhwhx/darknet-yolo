import serial as ser


class my_serial:
    def __init__(self):
        try:
            self.se=ser.Serial("/dev/ttyTHS1",115200,timeout=1)
            if self.se.is_open:
                print("serial is opened")
        except Exception as e:
            print('seial open faii',e)

    def open(self):
        try:
            self.se.open()
            print("serial is opened")
        except Exception as e:
            print('seial open faii',e)

    def close(self):
        try:
            self.se.close()
            print("serial is closed")
        except Exception as e:
            print('seial open faii',e)

    def send_data(self, data):
        self.se.write(data)
    
    def write_int(self, data):
        b = hex(data)[2:]
        while len(b)<4:
            b='0'+b
        for i in range(0, len(b), 2):
            self.se.write(bytes.fromhex(b[i]+b[i+1]))


def main():
    se=my_serial()
    se.send_data("777".encode('utf-8'))
    se.close()

if __name__=="__main__":
    main()


