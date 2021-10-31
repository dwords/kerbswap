#!/usr/bin/env python3
import os
import sys
import time
from time import sleep
import subprocess 
import contextlib



def ustat():
    if not os.geteuid() == 0:
        sys.exit("\nKerbswap needs root to run.\n")


def ui(): 

    print("=======K========")
    print("   KERBSWAP")
    print("=======S========")



def main():
    print("Your kernel version")
    ckv = os.system("uname -r" "| cut -f1 -d""-" ">" "ulv.txt")
    print("Checking for updates ......")
    
    with contextlib.redirect_stdout(None):
      
      os.system("curl https://raw.githubusercontent.com/dwords/remote-resources/main/vinvc/lkv.txt --output lkv.txt")
    sleep(6)

    c1=open("ulv.txt", "r")
    c2=open("lkv.txt", "r")
    for line1 in c1:
        for line2 in c2:
            if line1==line2:
                print("Your Kernel is up to date!.")
            else:
                print("Kernel is now upgrading....")
                os.system("rm -f lkv.txt")
                os.system("rm -f ulv.txt")
                subprocess.run(["./kerbswap.sh"])
        






ustat()
ui()
main()
