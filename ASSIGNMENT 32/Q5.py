'''
5. Write a program that deletes all empty files from a specified directory every hour.

The program should:

Scan the directory recursively.
Detect files whose size is zero bytes.
Delete the empty files.
Store deleted file paths in a log file.
Handle permission errors.

Note: Test the program only on a sample directory.
'''
import os
import schedule
import time

def DeleteEmptyFiles(Directory):

    if os.path.exists(Directory) == False:
        print("Directory does not exist")
        return

    fobj = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileList in os.walk(Directory):

        for fname in FileList:

            FilePath = os.path.join(FolderName, fname)

            try:
                if os.path.getsize(FilePath) == 0:
                        os.remove(FilePath)
                        print(fname, "Deleted")
                        fobj.write(FilePath + " Deleted\n")

            except PermissionError:
                print(fname, "Permission Denied")
                fobj.write(FilePath + " Permission Denied\n")

    fobj.close()


def main():

    Directory = input("Enter directory : ")

    
    DeleteEmptyFiles(Directory)

    
    schedule.every(1).hours.do(DeleteEmptyFiles, Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()