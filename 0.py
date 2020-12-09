import datetime
import sys
import re

if __name__ == "__main__":
    yy = r'[0-9]*年'
    mm = r'[0-9]*月'
    dd = r'[0-9]*日'
    num = r'[0-9]*'
    time = '2020年1月11日'
    clock1 = '10:30-12:30'
    print(re.findall(yy, time)[0][0:4])
    print(re.findall(mm, time)[0][0:1])
    print(re.findall(dd, time)[0][0:2])
    print(re.split('-', clock1))
    clock = re.split('-', clock1)
    bc = re.split(':', clock[0])
    bch = bc[0]
    bcm = bc[1]
    ec = re.split(':', clock[1])
    ech = ec[0]
    ecm = ec[1]
    print(bch, bcm)
    print(ech, ecm)
