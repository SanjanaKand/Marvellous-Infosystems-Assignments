
import smtplib
import os
from email.message import EmailMessage


def SendMail(ToMail, FileName):

    try:

        SenderMail = "sanjanakand31@gmail.com"
        Password = "ejbr hqbn jhpj bsre"

        Message = EmailMessage()

        Message["From"] = SenderMail
        Message["To"] = ToMail
        Message["Subject"] = "Guru Purnima Wishes and Process Information Log"

        Message.set_content(
            "Respected Sir,\n\n"
            "Happy Guru Purnima!\n\n"
            "On this auspicious occasion, I would like to express my heartfelt "
            "gratitude for your guidance, support, and valuable teachings. "
            "Thank you for inspiring us and helping us grow in our learning journey.\n\n"
            "Please find the attached Process Information Log file generated "
            "by my automation script as per the assignment.\n\n"
            "Wishing you good health, happiness, and continued success.\n\n"
            "Thank You.\n\n"
            "Regards,\n"
            "Sanjana Kand"
        )

        with open(FileName, "rb") as fobj:

            Data = fobj.read()

        Message.add_attachment(
            Data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(FileName)
        )

        Server = smtplib.SMTP("smtp.gmail.com", 587)

        Server.ehlo()
        Server.starttls()
        Server.ehlo()

        Server.login(SenderMail, Password)

        Server.send_message(Message)

        Server.quit()

        print("Mail sent successfully.")

    except Exception as e:

        print("Unable to send mail.")
        print("Error :", e)


def main():
    pass


if __name__ == "__main__":
    main()