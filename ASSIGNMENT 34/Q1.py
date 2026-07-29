'''
Automation Assignment

Please follow below rules while designing automation script as

• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

1. Design automation script which display information of running processes as its name, PID, Username.

Usage :
python ProcInfo.py
'''

import ModuleQ1
import sys


def main():

    Border = "-" * 60

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script displays information")
            print("of all running processes.")
            print("It stores Process Name, PID and Username")
            print("in ProcessLog.txt")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print(f"python {sys.argv[0]}")

        else:

            print("Unable to proceed as there is no matching argument.")
            print("Please use --h or --u flag.")

    elif(len(sys.argv) == 1):

        ModuleQ1.DisplayProcesses()

        print(Border)
        print("Process information stored successfully in ProcessLog.txt")
        print(Border)

    else:

        print("Invalid number of arguments.")
        print("Please use --h or --u flag.")

    print(Border)
    print("--- Thank you for using our automation system ---")
    print(Border)


if __name__ == "__main__":
    main()