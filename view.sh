#!/bin/sh
objdump -d dummy -M intel | grep -v "mov    r10," | grep -v "movabs r10," | grep -v "00 00 00"  | grep -Po "(?<=cmp    al\,)0x[0-f]{2}" | python3 -c 'lines = open(0); [print(chr(int(li[2:4], 16)), end="") for li in lines]'
