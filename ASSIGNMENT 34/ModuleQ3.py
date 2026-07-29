import psutil
import os
from datetime import datetime


def CreateLog(DirectoryName):

    try:

        if not os.path.exists(DirectoryName):
            os.mkdir(DirectoryName)

        if not os.path.isdir(DirectoryName):
            print("Entered path is not a directory.")
            return

        CurrentTime = datetime.now()

        FileName = os.path.join(DirectoryName, "ProcessLog3.txt")

        with open(FileName, "w") as fobj:

            fobj.write("Process Information Log\n")
            fobj.write(f"Log Created : {CurrentTime}\n")
            fobj.write("-" * 60 + "\n")

            for process in psutil.process_iter():

                try:

                    info = process.as_dict(attrs=['pid', 'name', 'username'])

                    fobj.write(f"Process Name : {info['name']}\n")
                    fobj.write(f"PID          : {info['pid']}\n")
                    fobj.write(f"Username     : {info['username']}\n")
                    fobj.write("-" * 60 + "\n")

                except (psutil.NoSuchProcess,
                        psutil.AccessDenied,
                        psutil.ZombieProcess):
                    pass

            fobj.write("Process information collected successfully.\n")
            fobj.write("-" * 60 + "\n")
            fobj.write("End of Log File\n")

    except Exception as e:

        print(f"Error : {e}")