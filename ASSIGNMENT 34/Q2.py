'''
2. Design automation script which accept process name and display information of that process if it is running.
   Usage : ProcInfo.py Notepad
'''

'''
2. Design automation script which accept process name and display
information of that process if it is running.

Usage :
python ProcInfo.py Notepad.exe
'''

import ModuleQ2
import sys


def main():

    if(len(sys.argv) != 2):

        print("Invalid number of arguments.")
        print(f"Usage : python {sys.argv[0]} ProcessName")
        return

    ProcessName = sys.argv[1]

    ModuleQ2.SearchProcess(ProcessName)


if __name__ == "__main__":
    main()