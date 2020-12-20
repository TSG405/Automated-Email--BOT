import smtplib
from email.message import EmailMessage

def send_email(receiver, subject, message):
    
    # SMTP Server Activation
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Authentication
    server.login('..Your Email (SENDER) Goes Here..', '..Your Email_password (SENDER) Goes Here..')
    
    email = EmailMessage()
    
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    
    # Initiation
    email.set_content(message)
    
    # Run through..
    server.send_message(email)

# Driver Function..  
def main():
    print("\n ---**--- Welcome to E-MAIL BOT ---**--- \n")
  
    receiver = input("To whom you want to send your E-MAIL (FORMAT: XYZ@gmail.com) ?? \t").lower()
    if "gmail.com" not in name.split('@'):
       print("ERROR! EMAIL ADDRESS IN WRONG FORMAT!\n")
       main()
    else:
       print("RECEIVER mail address: \t",)
     
    sub = input("\nWhat is the subject of your E-MAIL ?\t")
    body = input("\nOK.. What's the body of your E-mail? Type here [Upon finishing hit --> ENTER :] \t)
    send_email(receiver, sub, body)
    print("\n Mail Sent succesfully! ")
    user = input("Want to send another E-MAIL ? Type: [YES/Y/NO/N] \t")
    if (user.lower() == "yes" or user.lower() == "y"):
       main()
       
main()


    
@ CODED BY TSG405, 2020 
