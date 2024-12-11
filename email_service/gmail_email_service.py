from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import os

# Escopo necessário para enviar e-mails
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_email_service():
    """Autentica e retorna o serviço da API de envio de e-mails."""
    creds = None
    if os.path.exists('email_token.json'): 
        creds = Credentials.from_authorized_user_file('email_token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('email_credentials.json', SCOPES)  # Nome genérico
            creds = flow.run_local_server(port=0)
        with open('email_token.json', 'w') as token:
            token.write(creds.to_json())
    return build('email_service', 'v1', credentials=creds) 

def create_email(sender, recipient, subject, body):
    """Cria uma mensagem de e-mail no formato MIME."""
    message = MIMEText(body, 'html')
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_email(service, sender, recipient, subject, body):
    """Envia um e-mail usando a API de envio de e-mails."""
    message = create_email(sender, recipient, subject, body)
    try:
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Email enviado! ID da mensagem: {sent_message['id']}")
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
