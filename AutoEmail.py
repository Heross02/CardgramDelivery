# AutoEmail.py
import os
import win32com.client


def generate_outlook_email(recipient, subject, body, attachment_img, attachment_file):
    outlook_app = win32com.client.Dispatch("Outlook.Application")
    mail_item = outlook_app.CreateItem(0)  # 0 represents the MailItem type

    # Set email properties
    mail_item.To = recipient
    mail_item.Subject = subject
    mail_item.HTMLBody = body

    # Add the image
    attachment = mail_item.Attachments.Add(os.getcwd() + "\\" + f"{attachment_img}")
    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "template_img")

    # Adds downloadable img attachment
    mail_item.Attachments.Add(os.getcwd() + "\\" + f"{attachment_img}")

    # Adds downloadable file attachment
    mail_item.Attachments.Add(os.getcwd() + "\\" + f"{attachment_file}")

    # Send the email
    mail_item.Send()
