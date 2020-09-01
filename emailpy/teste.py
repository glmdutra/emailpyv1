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
           [sg.Text('Anexos', size=(10,0)), sg.Input(), sg.FileBrowse()],
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
                return(values[0], values[1], values[2], values[3], values[4], values[5]) # Retorna os três valores como uma tupla.

tela = TelaEmail()
sender_email1, password1, receiver_email1, title, message1, Anexos = tela.run() # Aqui tu faz o unpack da tua tupla em variáveis



def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return
    ctype, encoding = mimetypes.guess_type(filename)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    elif maintype == 'image':
        with open(filename, 'rb') as f:
            mime = MIMEImage(f.read(), _subtype=subtype)
    elif maintype == 'audio':
        with open(filename, 'rb') as f:
            mime = MIMEAudio(f.read(), _subtype=subtype)
    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())
        encoders.encode_base64(mime)
    
    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)



#COMMANDS EMAIL::


sender_email = sender_email1
receiver_email = "glmdutradesouza@gmail.com"
password = password1
receiver_email = receiver_email1

message = MIMEMultipart()
message["Subject"] = title
message["From"] = sender_email1
message["To"] = receiver_email1

# Create the plain-text and HTML version of your message
text = message1
html = message1
image = Anexos  
audio = Anexos



# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)
adiciona_anexo(message, "imagem.jpg")






# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email1, password1)
    server.sendmail(
        sender_email1, receiver_email1, message.as_string()
    )











"""
de = 'glmdutradesouza@gmail.com'
para = ['guilhermesouza_2@hotmail.com']
msg = MIMEMultipart()
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'SempreUpdate'
# Corpo da mensagem
msg.attach(MIMEText('Exemplo de email HTML com anexo do &lt;b&gt;SempreUpdate&lt;b/&gt;.', 'html', 'utf-8'))
# Arquivos anexos.
adiciona_anexo(msg, 'texto')
adiciona_anexo(msg, 'imagem')
raw = msg.as_string()
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('glmdutradesouza@gmail.com', '36980293STRANg')
smtp.sendmail(de, para, raw)
smtp.quit()"""