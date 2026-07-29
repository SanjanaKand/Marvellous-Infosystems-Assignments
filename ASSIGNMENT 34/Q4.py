'''
4. Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail.

   Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com

   Demo is name of Directory.
   marvellousinfosystem@gmail.com is the mail id.
'''
import ModuleQ4
import MailSender
import sys


def main():

    if(len(sys.argv) != 3):

        print("Invalid number of arguments.")
        print(f"Usage : python {sys.argv[0]} DirectoryName EmailID")
        return

    DirectoryName = sys.argv[1]
    EmailID = sys.argv[2]

    FileName = ModuleQ4.CreateLog(DirectoryName)

    if(FileName != None):

        MailSender.SendMail(EmailID, FileName)


if __name__ == "__main__":
    main()