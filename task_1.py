import time
import sys


class TrafficLight:
    __collor = "red"

    def running(self):
        print(TrafficLight.__collor, end="")
        sys.stdout.flush()
        time.sleep(7)

        self.__collor = "yellow"
        print(f"\r{self.__collor}", end="")
        sys.stdout.flush()
        time.sleep(2)

        self.__collor = "green"
        print(f"\r{self.__collor}", end="")
        sys.stdout.flush()
        time.sleep(5)

        print(f"\r ", end="")


t = TrafficLight()
t.running()
