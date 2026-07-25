'''
4. Write a program that copies all .txt files from one directory to another every ten minutes.

The program should:

Accept source and destination directories.
Validate both directories.
Copy only .txt files.
Maintain a log of copied files.
Avoid terminating if one file cannot be copied.
'''
import os
import shutil
import schedule
import time

def CopyFiles(Source, Destination):

    if os.path.exists(Source) == False:
        print("Source directory does not exist")
        return

    if os.path.exists(Destination) == False:
        print("Destination directory does not exist")
        return

    fobj = open("CopyLog.txt", "a")

    for file in os.listdir(Source):

        if file.endswith(".txt"):

            try:
                SourceFile = os.path.join(Source, file)
                shutil.copy(SourceFile, Destination)
                print(file, "Copied")
                fobj.write(file + " Copied Successfully\n")

            except:
                print(file, "Cannot be copied")
                fobj.write(file + " Copy Failed\n")

    fobj.close()



def main():

    Source = input("Enter source directory : ")
    Destination = input("Enter destination directory : ")

    CopyFiles(Source, Destination) 

    schedule.every(10).minutes.do(CopyFiles, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()