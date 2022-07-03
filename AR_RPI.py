import pyfirmata
import time

IGN = 4
SRT = 5
KSN = 7
PKL = 6
UNL = 8
LOC = 9
INL = 10
ACC = 11
global LocUL
global RunningFlag


try:
    board = pyfirmata.Arduino('/dev/ttyACM0')
    print("Communication Successfully started")
except:
    print("Relay Controller not connected")
else:

    board.digital[IGN].write(1)
    board.digital[SRT].write(1)
    board.digital[KSN].write(1)
    board.digital[PKL].write(1)
    board.digital[UNL].write(1)
    board.digital[LOC].write(1)
    board.digital[INL].write(1)
    board.digital[ACC].write(1)

    def StartCar():
        board.digital[KSN].write(0)
        time.sleep(1)
        board.digital[IGN].write(0)
        time.sleep(1)
        board.digital[SRT].write(0)
        time.sleep(1)
        board.digital[SRT].write(1)
        time.sleep(1)
        board.digital[PKL].write(0)
        time.sleep(1)
        board.digital[ACC].write(0)
        RunningFlag = 1
        return RunningFlag

    def StopCar():
        board.digital[KSN].write(1)
        board.digital[IGN].write(1)
        board.digital[SRT].write(1)
        board.digital[PKL].write(1)
        board.digital[ACC].write(1)
        # add rpm code
        RunningFlag = 0
        return RunningFlag

    def UnlockCar():
        board.digital[UNL].write(0)
        time.sleep(0.5)
        board.digital[UNL].write(1)
        time.sleep(0.5)
        board.digital[UNL].write(0)
        time.sleep(0.5)
        board.digital[UNL].write(1)
        time.sleep(0.5)
        LocUL = 1
        return LocUL

    def LockCar():
        board.digital[LOC].write(0)
        time.sleep(0.5)
        board.digital[LOC].write(1)
        time.sleep(0.5)
        board.digital[LOC].write(0)
        time.sleep(0.5)
        board.digital[LOC].write(1)
        time.sleep(0.5)
        LocUL = 0
        return LocUL

    def acc(accS):
        board.digital[ACC].write(accS)

    def inl(inlS):
        board.digital[INL].write(inlS)

    def pkl(pklS):
        board.digital[PKL].write(pklS)
        
StopCar()
