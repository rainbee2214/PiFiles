from ctypes import CDLL as c_dll
from ctypes import c_char_p as charPointer
from time import time
import os

getPiHex = c_dll(os.path.join(os.path.dirname(__file__), 'piqpr8.so')).getPiHex
getPiHex.restype = charPointer

def getHexFromIndex(index):
    """Gets the hexadecimal representation of pi proceeding the index.

    Note that accuracy stops at around 11.8 million

    Args:
        index: an integer >= 0 where you want the hex of pi afterwards

    Returns:
        A string representation of the 8 HEX digits proceeding index
        examlple for index 0: '243F6A88'
    """
    return getPiHex(index)

def verifyIndex(index):
    """Verifies the accuracy of the HEX representation pi proceeding the index.

    It achieves this goal by comparing the hex at index with index +/- 1.

    Args:
        index: an integer where you want to test the accuracy of hex of pi

    Returns:
        True or False if the given index is accurate
    """
    if index < 0:
        print "Index must be >= 0, returning False"
        return False
    elif index == 0:
        left = getHexFromIndex(0)[1:8]
        right = getHexFromIndex(1)[0:7]
        # print "index 0", left, right
        return left == right
    else:
        left = getHexFromIndex(index-1)
        middle = getHexFromIndex(index)
        right = getHexFromIndex(index+1)
        # print "index: " + str(index), left[1:8], middle[0:8], right[0:7]
        return left[1:8] == middle[0:7] and middle[1:8] == right[0:7]

def timedHex(index):
    """A Wrapper for getHexFromIndex to time the computation

    Args:
        index: an integer >= 0 where you want to test the pi computation

    Returns:
        None, prints a string outlining the time to completion
    """
    start = time()
    getHexFromIndex(index)
    end = time()
    print "Index", index, "took", end - start, "seconds"
