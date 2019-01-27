# This is pyhton script for monitoring bandwidh speed for your computer
# I make this script by the help of a python package called psutil
import time
import psutil

def main():
#set the initial value
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_mbit(value):
    return value/1024./1024.*8

def send_stat(value):
    print ("%0.3f" % convert_to_mbit(value))

main()
