import psutil
import os
from datetime import datetime


def CreateLog(DirectoryName):

    try:

        if(not os.path.exists(DirectoryName)):
            os.mkdir(DirectoryName)

        if(not os.path.isdir(DirectoryName)):
            print("Invalid Directory")
            return None

        CurrentTime = datetime.now()

        FileName = os.path.join(DirectoryName, "ProcessLog.txt")

        fobj = open(FileName, "w")

        fobj.write("Information of Running Processes\n")
        fobj.write(f"Log Created : {CurrentTime}\n")
        fobj.write("-" * 60 + "\n")

        for process in psutil.process_iter():

            try:

                info = process.as_dict(attrs=['pid', 'name', 'username'])

                fobj.write(f"Process Name : {info['name']}\n")
                fobj.write(f"PID          : {info['pid']}\n")
                fobj.write(f"Username     : {info['username']}\n")
                fobj.write("-" * 60 + "\n")

            except(psutil.NoSuchProcess,
                   psutil.AccessDenied,
                   psutil.ZombieProcess):

                pass

        fobj.write("Process information collected successfully.\n")

        fobj.close()

        return FileName

    except Exception as e:

        print("Unable to create log file.")
        print("Error :", e)

        return None