import smtplib
from email.message import EmailMessage

def send_email(receiver, subject, message):

    try:
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
        
    except:
        print("\n\n--------------------------------------------")
        print("BOT: !ERROR! Check your G-MAIL Security settings! and your NETWORK CONNECTIVITY! \n~Thank You")
        exit()
    

# Driver Function..  
def main():
    print("\n\n------------------------------------------")
    print("---**--- Welcome to E-MAIL BOT ---**---")
    print("------------------------------------------\n\n")
  
    receiver = input("BOT: To whom you want to send your E-MAIL (FORMAT: XYZ@gmail.com) ?? TYPE HERE: \t").lower()
    if "gmail.com" not in receiver.split('@'):
       print("BOT: ERROR! EMAIL ADDRESS IN WRONG FORMAT!\n")
       main()
    else:
       print("BOT: RECEIVER mail address: \t",receiver)
    print("--------------------------------------------")
    
    sub = input("\n\nBOT: Fine.. So, what is the \"SUBJECT\" of your E-MAIL ?? :\t")
    print("BOT: ACCEPTED!...")
    print("--------------------------------------------")
    
    body = input("\n\nBOT: OK.. What's the \"BODY\" of your E-MAIl ?? Type here [Upon finishing hit --> ENTER :] \t")
    print("BOT: Please Wait... Confirming Status **")
    
    send_email(receiver, sub, body)
    
    print("\n\n***********-----***********  Mail Sent succesfully!  ***********-----***********")
    
    user = input("\n\nBOT: Want to send another E-MAIL ? Type: [YES/Y/NO/N] \t")
    if (user.lower() == "yes" or user.lower() == "y"):
       main()


main()


@ CODED BY TSG405, 2020
