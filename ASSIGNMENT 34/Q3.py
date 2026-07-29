'''
3. Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username.

   Usage : ProcInfoLog.py Demo

   Demo is name of Directory.
'''

import ModuleQ3
import sys


def main():

    if(len(sys.argv) != 2):

        print("Invalid number of arguments.")
        print(f"Usage : python {sys.argv[0]} DirectoryName")
        return

    DirectoryName = sys.argv[1]

    ModuleQ3.CreateLog(DirectoryName)


if __name__ == "__main__":
    main()