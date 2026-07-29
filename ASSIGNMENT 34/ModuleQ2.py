import psutil
from datetime import datetime


def SearchProcess(ProcessName):

    try:

        fobj = open("ProcessLog2.txt", "w")

        CurrentTime = datetime.now()

        fobj.write("Process Information Log\n")
        fobj.write(f"Log Created : {CurrentTime}\n")
        fobj.write("-" * 60 + "\n")

        Found = False

        for process in psutil.process_iter():

            try:

                info = process.as_dict(attrs=['pid', 'name', 'username'])

                if ProcessName.lower() in info['name'].lower():

                    Found = True

                    fobj.write(f"Process Name : {info['name']}\n")
                    fobj.write(f"PID          : {info['pid']}\n")
                    fobj.write(f"Username     : {info['username']}\n")
                    fobj.write("-" * 60 + "\n")

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

        if Found == False:

            fobj.write(f"Process '{ProcessName}' is not running.\n")

        else:

            fobj.write("Process search completed successfully.\n")

        fobj.close()

    except Exception as e:

        print("Unable to create log file.")
        print("Error :", e)