import smtplib
import pyttsx3
import speech_recognition as tsg
from email.message import EmailMessage


engine = pyttsx3.init()

interpreter = tsg.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with tsg.Microphone() as source:
            print('\nSpeak! I am Listening...')
            voice = interpreter.listen(source)
            
            # Using Google API
            info = interpreter.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("\nError in Interpreting your voice! Try Again Later!\n")
        return 0
        

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


# Optional #
email_list = {
    'self': 'tasengupta405',
    'dark': '999darkcoder999@gmail.com',
    'friend': 'xyz@gmail.com'
}

# Driver Function..  
def main():
    print("\n ---**--- Welcome to E-MAIL BOT ---**--- \n")
    
    speak('Hey, user, to whom will you want to send email ?')
    name = get_info()
    if (name == 0):
        speak(' Error! Please try after sometime.. ')
        exit()
    
    receiver = email_list[name]
    print(receiver)
    
    speak('Okay, so what is the subject of your E-MAIL?? ')
    sub = get_info()
    
    Speak('Fine!, Tell me the body of your E-MAIL ')
    body = get_info()
    
    send_email(receiver, sub, body)
    
    print("\n Mail Sent succesfully! ")
    speak('Your email is sent successfully!')
    print("\nDo you want to send more email? SPEAK: [YES/NO]")
    speak('Do you want to send more email?')
    
    send_again = get_info()
    if 'yes' in send_again.lower():
        main()


main()


@ CODED BY TSG405, 2020 
