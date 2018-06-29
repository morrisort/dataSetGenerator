"""generate data set."""

from termios import tcflush, TCIFLUSH
import sys
import os
from pynput import keyboard
import datetime
import pathlib
import time
startTime = None

"""
This code was based on an example that can be found in:
https://pynput.readthedocs.io/en/latest/keyboard.html
"""

def findDataNumber(user, directory):
    """Search for the next data set number for 'user'."""
    i = 1
    while (True):
        dataPath = directory + "/data" + user + "_" + str(i) +".txt"
        if os.path.isfile(dataPath):
            i += 1
        else:
            print("Number of data sets found: {0}".format(i-1))
            print("Generating data set number {0} in path: '{1}'".format(i, dataPath))
            return dataPath


def on_press(key):
    timeStamp = (datetime.datetime.now() - startTime).total_seconds()
    try:
        if repr(key.char) == "None":  # for some reason, 'alt Gr' key has key.char
            return                    # but ord(key.char) wont work
        print('{0} pressed {1}'.format(key.char, timeStamp))
        outputData.write("{0}\tpressed \t{1}\n".format(ord(key.char), repr(timeStamp)))

    except AttributeError:
        if key == key.space:
            print('{0} pressed {1}'.format(key.value, timeStamp))
            outputData.write("32\tpressed \t{0}\n".format(repr(timeStamp)))
        else:
            print('{0} pressed {1}'.format(key.value, timeStamp))
            outputData.write("{0}\tpressed \t{1}\n".format((key.value), repr(timeStamp)))

def on_release(key):
    timeStamp = (datetime.datetime.now() - startTime).total_seconds()

    try:
        if repr(key.char) == "None": # for some reason, 'alt Gr' key has key.char
            return                   # but ord(key.char) wont work
        print('{0} released {1}'.format(key.char, timeStamp))
        outputData.write("{0}\treleased\t{1}\n".format(ord(key.char), repr(timeStamp)))
    except AttributeError:
        if key == key.space:
            print('{0} released {1}'.format(key.value, timeStamp))
            outputData.write("32\treleased \t{0}\n".format(repr(timeStamp)))
        else:
            print('{0} released {1}'.format(key.value, timeStamp))
            outputData.write(repr(key.value) + '\treleased\t' + repr(timeStamp) + '\n')
            if key == keyboard.Key.esc:
                outputData.close()
                return False

if len(sys.argv) != 3:
    print('Usage: {0} <path> <user>'.format(sys.argv[0]))
    raise SystemExit

directory = sys.argv[1]
user = sys.argv[2]
pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
dataPath = findDataNumber(user, directory)
outputData = open(dataPath, "w")
outputData.write('Key\tAction\t\tTimeStamp [s]\n')

print("Press Esc to exit program")

# to ensure that the 'enter' that started this script has been released
time.sleep(0.5)

startTime = datetime.datetime.now()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

    # check if dataset is valid

    # flushing input
    tcflush(sys.stdin, TCIFLUSH)

    while (True):
        validDataSet = input("Is the data set valid?[y/n]: ")
        if (validDataSet == "n"):
            print("the dataset will be erased")
            os.remove(dataPath)
            break
        elif (validDataSet == "y"):
            print ("Valid dataset!")
            break
        else:
            print ("input must be 'y' or 'n'")

		else :
			print ("input must be 'y' or 'n'")
