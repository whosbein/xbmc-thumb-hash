#! /usr/bin/env python2
import sys

def xbmc_thumb_hash(input):
    chars = input.lower()
    crc = 0xffffffff
    for ptr in chars:
        chr = ord(ptr)
        crc ^= chr << 24
        for i in range(8):
            if crc & 0x80000000:
                crc = (crc << 1) ^ 0x04c11db7
            else:
                crc <<= 1

    if crc >= 0:
        print "%08x" % (crc & 0xffffffff)
        #string = "%08x" % crc
        #print string[-8:]
        #print "%x" % crc
        #print crc
    else:
        print 'guh'

if __name__=="__main__":
    print sys.argv[1]
    xbmc_thumb_hash(sys.argv[1])
