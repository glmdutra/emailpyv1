import smtplib, ssl
import PySimpleGUI as sg
import mimetypes
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage



class TelaEmail:
    def __init__(self):

        sg.theme('DarkBlue')
        self.layout = [
           [sg.Text('Login Gmail:', size=(10,0)), sg.InputText()],
           [sg.Text('Senha Gmail:', size=(10,0)), sg.InputText(password_char='*')],
           [sg.Text('Destinatário:', size=(10,0)), sg.InputText()],
           [sg.Text('Título Email:', size=(10,0)), sg.InputText()],
           [sg.Text('Mensagem:', size=(10,0)), sg.InputText()],
           [sg.Button('Iniciar'), sg.Button('Cancelar')]
           
        ]

    
    def run(self):

        #Janela
        window = sg.Window("Dados do Email", self.layout)

        # Aqui eu coloco um EventLoop para o Iniciar e Cancelar
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                exit() # Aqui o user clicou em cancelar e o programa termitestena

            elif event == 'Iniciar':
                window.close()
                return(values[0], values[1], values[2], values[3], values[4]) # Retorna os três valores como uma tupla.

tela = TelaEmail()
sender_email1, password1, receiver_email1, title, message1 = tela.run() # Aqui tu faz o unpack da tua tupla em variáveis





#COMMANDS EMAIL::


sender_email = sender_email1
receiver_email = "glmdutradesouza@gmail.com"
password = password1
receiver_email = receiver_email1

message = MIMEMultipart("alternative")
message["Subject"] = title
message["From"] = sender_email1
message["To"] = receiver_email1

# Create the plain-text and HTML version of your message
text = message1
html = message1

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email1, password1)
    server.sendmail(
        sender_email1, receiver_email1, message.as_string()
    )