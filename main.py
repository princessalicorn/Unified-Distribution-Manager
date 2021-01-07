import argparse, shlex, subprocess
from pmconfig import *

#System Update Command
def sysupdate():
    for x in cmd:
        cmd1 = shlex.split(x)
        subprocess.run(cmd1) 
        stderr=subprocess.STDOUT
    
    if stderr != None:
        print("No Errors Reported... Exiting :)")
    else:
        print("Errors Have Occured, See Above... :(")

#The fun shit
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', action='store_true', help="Updates your system")
    args = parser.parse_args()
    if args.update:
        sysupdate()

if __name__ == '__main__':
    main()