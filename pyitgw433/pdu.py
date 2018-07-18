#!/usr/bin/env python

import fileinput
import codecs


head = "0,0,6,0,256,{pairs},0,1,10,1,"
hi = "5,1,"
lo = "1,1,"
down = hi + lo
up = lo + hi
end = "39,0"
space = lo + lo

class Pdu:
    def __init__(self, data):
        self._data = data

    def __str__(self):
        start = 0
        data = self._data
        pairs = (len(data.split(",")) / 2) - 3
        while start <= len(data):
            data = strip(data, head.format(**{"pairs": pairs}), "H" + str(pairs), start)
            data = strip(data, up, "|", start)
            data = strip(data, down, "_", start)
            data = strip(data, end, "E", start)
            data = strip(data, space, "o", start)
            start = start + 1
        return data

    def __len__(self):
        return len(self._data)

def strip(data, the_str, replace, start):
    if data.startswith(the_str, start):
        data = data[0:start] + replace + data[start + len(the_str):]
    return data

def parse_stdin():
    for line in fileinput.input():
        print str(Pdu(str(codecs.decode(line.strip(), "hex"))))
