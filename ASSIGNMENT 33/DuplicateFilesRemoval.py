import sys
import os
import hashlib
import time
import schedule

from EmailModule import SendMail



##########################################################
#
#   Function name :     CalculateChecksum
#   Input :             Name of File
#   Description :       Calculates MD5 checksum of given file
#                       and returns unique hash value
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def CalculateChecksum(FileName):

    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):

        hobj.update(Buffer)

        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()



##########################################################
#
#   Function name :     FindDuplicate
#   Input :             Name of Directory
#   Description :       Scans directory, calculates checksum
#                       and identifies duplicate files
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def FindDuplicate(DirectoryName):

    Duplicate={}

    TotalFiles=0

    ErrorList=[]


    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:

            try:

                fname=os.path.join(FolderName,fname)


                if(os.path.isfile(fname)==False):

                    continue


                TotalFiles=TotalFiles+1


                Checksum=CalculateChecksum(fname)


                if Checksum in Duplicate:

                    Duplicate[Checksum].append(fname)


                else:

                    Duplicate[Checksum]=[fname]


            except Exception as e:

                ErrorList.append(str(e))


    return Duplicate,TotalFiles,ErrorList




##########################################################
#
#   Function name :     UpdateEmailStatus
#   Input :             Log File Name, Email Status
#   Description :       Updates email delivery status
#                       inside log file
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def UpdateEmailStatus(LogFile,Status):

    fobj=open(LogFile,"a")

    Border="-"*60


    fobj.write("\n")

    fobj.write(Border+"\n")

    fobj.write("                   Email Status\n")

    fobj.write(Border+"\n\n")

    fobj.write(
        "Email Delivery Status : "
        +Status+"\n"
    )


    fobj.write(Border+"\n")


    fobj.close()

##########################################################
#
#   Function name :     DeleteDuplicate
#   Input :             Name of Directory
#   Description :       Finds duplicate files, deletes extra
#                       copies, creates log file and stores
#                       execution details
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def DeleteDuplicate(DirectoryName):


    if(os.path.exists(DirectoryName)==False):

        print("Directory does not exist")

        return None



    if(os.path.isdir(DirectoryName)==False):

        print("Invalid Directory")

        return None



    Start=time.time()



    if(os.path.exists("Marvellous")==False):

        os.mkdir("Marvellous")



    CurrentTime=time.localtime()

    TimeStamp=time.strftime(
        "%d_%m_%Y_%H_%M_%S",
        CurrentTime
    )


    LogFileName="DuplicateRemovalLog_"+TimeStamp+".log"


    LogPath=os.path.join(
        "Marvellous",
        LogFileName
    )



    fobj=open(LogPath,"w")


    Border="-"*60



    StartTime=time.ctime()



    fobj.write(Border+"\n")

    fobj.write(
        "        Duplicate File Removal Automation Log\n"
    )

    fobj.write(Border+"\n\n")


    fobj.write(
        "Directory Scanned : "
        +DirectoryName+"\n\n"
    )


    fobj.write(
        "Scanning Started : "
        +StartTime+"\n\n"
    )



    MyDict,TotalFiles,ErrorList=FindDuplicate(DirectoryName)



    Result=list(
        filter(
            lambda x:len(x)>1,
            MyDict.values()
        )
    )



    TotalDuplicate=0

    TotalDeleted=0



    for value in Result:


        Checksum=CalculateChecksum(value[0])


        fobj.write(Border+"\n")

        fobj.write(
            "Duplicate Files Found\n"
        )

        fobj.write(Border+"\n\n")


        fobj.write(
            "Checksum Value : "
            +Checksum+"\n\n"
        )


        Count=0



        for subvalue in value:


            Count=Count+1



            if(Count==1):


                fobj.write(
                    "Original File:\n"
                )

                fobj.write(
                    subvalue+"\n\n"
                )


            else:


                fobj.write(
                    "Duplicate File Deleted:\n"
                )


                fobj.write(
                    subvalue+"\n\n"
                )



                TotalDuplicate=TotalDuplicate+1


                try:


                    os.remove(subvalue)


                    TotalDeleted=TotalDeleted+1


                except Exception as e:


                    ErrorList.append(str(e))



    EndTime=time.ctime()

    End=time.time()



    fobj.write(Border+"\n")

    fobj.write(
        "                Execution Summary\n"
    )

    fobj.write(Border+"\n\n")



    fobj.write(
        "Total Files Scanned : "
        +str(TotalFiles)+"\n"
    )


    fobj.write(
        "Total Duplicate Files Found : "
        +str(TotalDuplicate)+"\n"
    )


    fobj.write(
        "Total Duplicate Files Deleted : "
        +str(TotalDeleted)+"\n\n"
    )



    fobj.write(
        "Scanning Completed : "
        +EndTime+"\n\n"
    )


    fobj.write(
        "Execution Duration : "
        +str(round(End-Start,2))
        +" seconds\n\n"
    )



    fobj.close()



    return LogPath






##########################################################
#
#   Function name :     main
#   Input :             Command Line Arguments
#   Description :       Accepts directory, interval and email
#                       and controls automation execution
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def main():

    Border="-"*40


    print(Border)

    print(
        "Marvellous Automation Script"
    )

    print(Border)



    if(len(sys.argv)>=2):


        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):


            print(
                "This script identifies and removes duplicate files."
            )

            print(
                "Usage : python DuplicateRemoval.py DirectoryName TimeInterval Email"
            )


            return



        elif(sys.argv[1]=="--U" or sys.argv[1]=="--u"):


            print(
                "Usage : python DuplicateRemoval.py DirectoryName TimeInterval Email"
            )

            print(
                "Example : python DuplicateRemoval.py Test 5 abc@gmail.com"
            )


            return



        else:



            if(len(sys.argv)!=4):

                print(
                    "Invalid number of arguments"
                )

                return



            DirectoryName=sys.argv[1]



            try:

                Interval=int(sys.argv[2])


            except Exception:

                print(
                    "Invalid time interval"
                )

                return




            if(Interval<=0):

                print(
                    "Time interval should be positive"
                )

                return




            if(os.path.exists(DirectoryName)==False):

                print(
                    "Directory does not exist"
                )

                return




            if(os.path.isdir(DirectoryName)==False):

                print(
                    "Invalid Directory"
                )

                return




            schedule.every(Interval).minutes.do(
                DeleteDuplicate,
                DirectoryName
            )



            LogFile=DeleteDuplicate(
                DirectoryName
            )



            print(
                "Log File Created : ",
                LogFile
            )



            Status=SendMail(
                sys.argv[3],
                LogFile
            )



            print(Status)



            UpdateEmailStatus(
                LogFile,
                Status
            )



            while True:


                schedule.run_pending()

                time.sleep(1)



    else:


        print(
            "Invalid number of arguments"
        )

        print(
            "Use -h or -u for help"
        )



    print(Border)

    print(
        "ThankYou for using Marvellous Automation Script"
    )

    print(Border)


##########################################################
#
#   Starter of the Automation Script
#
##########################################################

if __name__=="__main__":

    main()