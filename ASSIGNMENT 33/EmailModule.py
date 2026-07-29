import smtplib
import os
from email.message import EmailMessage



##########################################################
#
#   Function name :     SendMail
#   Input :             Receiver Email, Log File Name
#   Description :       Sends duplicate removal log file
#                       through email notification
#   Date :              29/07/2026
#   Author :            Sanjana Kand
#
##########################################################

def SendMail(ToMail, FileName):

    try:

        SenderMail = "sanjanakand31@gmail.com"

        Password = "vztb hylm jzqf wsbi"


        Message = EmailMessage()


        Message["From"] = SenderMail

        Message["To"] = ToMail

        Message["Subject"] = "Duplicate File Removal Automation Log"



        Message.set_content(
            "Respected Sir,\n\n"
            "The Duplicate File Removal Automation Script has been executed "
            "successfully.\n\n"
            "The script scanned the given directory, identified duplicate files, "
            "removed duplicate files, and generated the execution log file.\n\n"
            "Please find the attached Duplicate Removal Log file generated "
            "by my automation script.\n\n"
            "Thank You.\n\n"
            "Regards,\n"
            "Sanjana Kand"
        )



        with open(FileName,"rb") as fobj:

            Data = fobj.read()



        Message.add_attachment(
            Data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(FileName)
        )



        Server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )


        Server.ehlo()

        Server.starttls()

        Server.ehlo()



        Server.login(
            SenderMail,
            Password
        )


        Server.send_message(Message)


        Server.quit()



        return "Mail sent successfully."



    except Exception as e:


        return "Unable to send mail. Error : "+str(e)




####################################################################
#
# main()
#
####################################################################

def main():

    pass



if __name__ == "__main__":
    main()