import pyttsx3
import smtplib
import speech_recognition as tsg
from email.message import EmailMessage


engine = pyttsx3.init()

interpreter = tsg.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Taking User's Input..
def get_info():

    try:
        with tsg.Microphone() as source:
            print('\nSpeak! I am Listening...')
            v = interpreter.listen(source)
            
            # Using Google API
            info = interpreter.recognize_google(v)
            print(info)
            return info.lower()
    except:
        print("\nError in Interpreting your voice! Try Again Later! ~Thank You")
        return 0
        

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
        speak('ERROR! Check your G-MAIL Security settings and your NETWORK CONNECTIVITY. Thank You')
        exit()


# Optional #
email_list = {
    'self': 'tasengupta405',
    'dark': '999darkcoder999@gmail.com',
    'friend': 'xyz@gmail.com'
}

# Driver Function..  
def main():
    print("\n\n------------------------------------------")
    print("---**--- Welcome to E-MAIL BOT ---**---")
    print("------------------------------------------\n\n")

    print("BOT: Hey! User, to whom will you want to send email ?? :\t")
    speak('Hey, user, to whom will you want to send your email ?')
    name = get_info()
    
    if (name == 0):
        speak('Error! Please try after sometime.. ')
        exit()
    
    receiver = email_list[name]
    print("BOT: RECEIVER mail address: \t",receiver)
    print("--------------------------------------------")

    print("\n\nBOT: Fine.. Okay, so what is the \"SUBJECT\" of your E-MAIL ?? :\t")
    speak('Fine, okay, so what is the subject of your E-MAIL?? ')
    sub = get_info()
    print("BOT: ACCEPTED!...")
    print("--------------------------------------------")

    print("\n\nBOT: OK.. Tell me the \"BODY\" of your E-MAIl ?? :\t")
    Speak('Okay, Tell me the body of your E-MAIL ')
    body = get_info()

    print("BOT: Please Wait... Confirming Status **")
    send_email(receiver, sub, body)
    
    print("\n\n***********-----***********  Mail Sent successfully!  ***********-----***********")
    speak('Your email is sent successfully!')
    
    print("\n\nBOT: Want to send another E-MAIL ? SPEAK: [YES/NO] \t")
    speak('Do you want to send another email?')
    
    send_again = get_info()
    if ('yes' in send_again.lower()):
        main()


main()


@ CODED BY TSG405, 2020
