import psutil
from datetime import datetime


def DisplayProcesses():

    try:

        fobj = open("ProcessLog1.txt", "w")

        CurrentTime = datetime.now()

        fobj.write("Process Information Log\n")
        fobj.write("Log Created : " + str(CurrentTime) + "\n")
        fobj.write("-" * 60 + "\n")

        for process in psutil.process_iter():

            try:

                info = process.as_dict(attrs=['pid', 'name', 'username'])

                fobj.write("Process Name : " + str(info['name']) + "\n")
                fobj.write("PID          : " + str(info['pid']) + "\n")
                fobj.write("Username     : " + str(info['username']) + "\n")
                fobj.write("-" * 60 + "\n")

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):

                pass

        fobj.write("Process information collected successfully.\n")
        fobj.write("End of Log File.\n")

        fobj.close()

    except Exception as e:

        print("Unable to create log file")
        print("Error :", e)