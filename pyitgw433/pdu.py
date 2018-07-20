#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from builtins import str
from builtins import object
import fileinput
import codecs


# Don't know the meaning of these. I've figured these things out by capturing
# traffic that my Android mobile app sends, looking at some other code on
# the internet, logic and general protocol knowledge (e.g. you tend to comminicate
# protocol versions up front and not at the end as some code on the internet suggests)
# and trial and error. The only part that changes for me is
# the amount of pairs of digits sent after the header. The amount of
# pairs includes the two pairs in this header here after the pair count
head = "0,0,6,0,256,{pairs},0,1,10,"
head2 = "0,0,6,0,360,{pairs},0,"
high = "1,5,"
high2 = "3,1,"
low = "1,1,"
low2 = "1,3,"
# The "high" value never appears twice in a row so only these pairs of pairs are valid
down = high + low
down2 = low2 + low2
up = low + high
up2 = low2 + high2
space = low + low
# This is how the data always seems to end
end = "1,39,0"
end2 = "1,31,0"

class Pdu(object):
    def __init__(self, data):
        if isinstance(data, list):
            self._data = ",".join([str(x) for x in data])
        else:
            self._data = data

    def __str__(self):
        """ Converts the raw protocol message into something that is easier to analyze
        """
        start = 0
        data = self._data
        pairs = int(len(data.split(",")) / 2) - 3
        while start <= len(data):
            data = strip(data, head.format(**{"pairs": pairs}), "H" + str(pairs), start)
            data = strip(data, head2.format(**{"pairs": pairs}), "h" + str(pairs), start)
            data = strip(data, up, "|", start)
            data = strip(data, up2, "|", start)
            data = strip(data, down, "_", start)
            data = strip(data, down2, "_", start)
            data = strip(data, end, "E", start)
            data = strip(data, end2, "E", start)
            data = strip(data, space, "o", start)
            start = start + 1
        return data

    def __len__(self):
        return len(self._data)

def wheel_to_str(letter):
    num = ord(letter.upper()) - ord("A")
    return be_num_to_str(num)

def be_num_to_str(num):
    return num_to_str(num, be_bit_range)

def se_num_to_str(num):
    return num_to_str(num, se_bit_range)

def num_to_str(num, rangefunc):
    if num < 0 or num > 15:
        return down + down + down + down
    ret = ""
    for i in rangefunc():
        if (1 << i) & num != 0:
            ret = ret + up
        else:
            ret = ret + down
    return ret

def be_bit_range():
    return range(0, 4)

def se_bit_range():
    return [3-x for x in range(0, 4)]

def strip(data, the_str, replace, start):
    if data.startswith(the_str, start):
            data = data[0:start] + replace + data[start + len(the_str):]
    return data

def parse_stdin():
    for line in fileinput.input():
        print(str(Pdu(str(codecs.decode(line.strip(), "hex")))))
